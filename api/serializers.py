from rest_framework import serializers
from .models import (Partners, Courses_Category, Payment_Modality, Courses, People_Interested, Provinces, Cantons, Districts, 
                     Neighborhoods, Genre, Student_Status, Identifications, Form, Administrator, Student, Enrollment, 
                     Payment_Methods, Payment, CourseModality, Student_Courses, Student_Payments,Event, Blog)
from django.contrib.auth.models import User, Group
import re
from django.core.exceptions import ValidationError
from datetime import date
from django.utils import timezone


class UserStudentRegisterSerializer(serializers.ModelSerializer):
    # Campo 'role' es opcional, pero solo se usa en escritura si se provee
    role = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        # Campos que se incluirán en la serialización
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'role')

    def validate_password(self, value):
        # Validación para asegurar que la contraseña tenga al menos 6 caracteres
        if len(value) < 2:
            raise serializers.ValidationError("La contraseña debe tener al menos 6 caracteres.")
        return value

    def create(self, validated_data):
        # Extraer el rol si está presente, o asignar 'student' como predeterminado
        role = validated_data.pop('role', 'student')
        # Crear una instancia de User con los datos validados
        user = User(**validated_data)
        # Establecer la contraseña encriptada
        user.set_password(validated_data['password'])
        # Guardar el usuario en la base de datos
        user.save()
        # Asignar el rol al grupo correspondiente (student por defecto)
        try:
            group = Group.objects.get(name=role)
            user.groups.add(group)
        except Group.DoesNotExist:
            raise serializers.ValidationError(f"El rol '{role}' no existe.")
        return user
    
    def update(self, instance, validated_data):
        # Actualizar los campos del usuario con los datos proporcionados
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        # Verificar si se está actualizando el correo electrónico
        new_email = validated_data.get('email', instance.email)
        if new_email != instance.email:
            # Validar que el nuevo correo no esté siendo usado por otro usuario
            if User.objects.filter(email=new_email).exists():
                raise ValidationError("Este correo electrónico ya está en uso por otro usuario.")
            # Si el correo no está en uso, asignarlo
            instance.email = new_email
        # Si se proporciona una nueva contraseña, establecerla
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        # Guardar la instancia del usuario
        instance.save()
        return instance

#############################################################################################

class UserAdminRegisterSerializer(serializers.ModelSerializer):
    # Campo 'role' es opcional, pero solo se usa en escritura si se provee
    role = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        # Campos que se incluirán en la serialización
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'role')
    
    def create(self, validated_data):
        # Extraer el rol si está presente, o asignar 'admin' como predeterminado
        role = validated_data.pop('role', 'admin')
        # Crear una instancia de User con los datos validados
        user = User(**validated_data)
        # Establecer la contraseña encriptada
        user.set_password(validated_data['password'])
        # Guardar el usuario en la base de datos
        user.save()
        # Asignar el rol al grupo correspondiente (admin por defecto)
        try:
            group = Group.objects.get(name=role)
            user.groups.add(group)
        except Group.DoesNotExist:
            raise serializers.ValidationError(f"El rol '{role}' no existe.")

        return user
    def update(self, instance, validated_data):
        # Actualizar los campos del usuario con los datos proporcionados
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        # Verificar si se está actualizando el correo electrónico
        new_email = validated_data.get('email', instance.email)
        if new_email != instance.email:
            # Validar que el nuevo correo no esté siendo usado por otro usuario
            if User.objects.filter(email=new_email).exists():
                raise ValidationError("Este correo electrónico ya está en uso por otro usuario.")
            # Si el correo no está en uso, asignarlo
            instance.email = new_email
        # Si se proporciona una nueva contraseña, establecerla
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        # Guardar la instancia del usuario
        instance.save()
        return instance

##################### PARTNERS / ALIANZAS#####################
class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

################## MODALIDAD DE PAGO###################
class PaymentModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Modality
        fields = '__all__'

    # Validación de un campo específico, por ejemplo, 'name' no debe ser vacío
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de la modalidad de pago no puede estar vacío")
        return value

################ CATEGORIA DEL CURSO ######################
class Courses_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses_Category
        fields = '__all__'

    def validate_category_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de la categoría no puede estar vacío")
        

################     CURSOS    #####################################
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        
    # Validación para un campo específico
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre del curso no puede estar vacío")

    def validate_duration(self, value):
        #Valida que la duración del curso sea positiva
        if value <= 0:
            raise serializers.ValidationError("La duración debe ser mayor que 0")
        return value
    
    def validate(self, data):
        #Valida las relaciones entre campos, por ejemplo, asegurarse de que el campo 'start_date' no sea posterior al campo 'end_date'
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        return data
    

################ PERSONAS INTERESADAS ##############################
class People_InterestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = People_Interested
        fields = '__all__'

    # Validación para el nombre
    def validate_person_name(self, value):
        # Validar que el nombre no contenga números
        if re.search(r'\d', value):
            raise serializers.ValidationError("El nombre no puede contener números.")
        return value

    # Validación para el apellido
    def validate_person_first_last_name(self, value):
        # Validar que el apellido no contenga números
        if re.search(r'\d', value):
            raise serializers.ValidationError("El apellido no puede contener números.")
        return value

    # Validación para el número de teléfono
    def validate_person_phone_number(self, value):
        if len(value) < 7 or len(value) > 20:
            raise serializers.ValidationError("El número de teléfono debe tener entre 8 y 20 dígitos.")
        return value

    # Validación para las notas
    def validate_person_notes(self, value):
        # Asegurarse de que las notas no excedan el límite de caracteres
        if len(value) > 150:
            raise serializers.ValidationError("Las notas no pueden exceder los 150 caracteres.")
        return value

    # Validación para el curso
    def validate_course(self, value):
        # Asegurarse de que el nombre del curso no sea demasiado largo
        if len(value) > 50:
            raise serializers.ValidationError("El nombre del curso no puede exceder los 50 caracteres.")
        return value


################     PROVINCIA    ##################
class ProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinces
        fields = '__all__'
        
###############       CANTONES      #################
class CantonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cantons
        fields = '__all__'
               
###############        DISTRITOS    ################
class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'
        
##############        BARRIOS        ################
class NeighborhoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhoods
        fields = '__all__'

#############         GÉNERO          #################
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
    

############      ESTADO DEL ESTUDIANTE    #############
class Student_StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Status
        fields = '__all__'


 ############     TIPO DE IDENTIFICACIONES   #############
class IdentificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifications
        fields = '__all__'


# FORMULARIO DE PREMATRÍCULA
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

    # Validación de identificación única
    def validate_identification_number(self, value):
        if not value:
            raise serializers.ValidationError("El número de identificación no puede estar vacío.")
        return value
    
    # Validación de fecha de nacimiento (mayor de 14 años)
    def validate_birth_date(self, value):
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 14:
            raise serializers.ValidationError("La edad debe ser de al menos 14 años.")
        return value
    
    # Validación de número de teléfono (solo números y con longitud adecuada)
    def validate_phone_number(self, value):
        if not re.match(r'^\+?\d{8,15}$', value):
            raise serializers.ValidationError("El número de teléfono debe tener entre 8 y 15 dígitos.")
        return value
    
    # Validación de la existencia de las claves foráneas
    def validate_identification_fk(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'identification_fk' es obligatorio.")
        return value
    
    def validate_genre_fk(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'genre_fk' es obligatorio.")
        return value
    
    def validate_course_fk(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'course_fk' es obligatorio.")
        return value
    
    def validate_student_status_fk(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'student_status_fk' es obligatorio.")
        return value

    # Validación de campo de dirección
    def validate_address(self, value):
        if value and len(value) < 4:
            raise serializers.ValidationError("La dirección es demasiado corta. Debe ser al menos de 4 caracteres.")
        return value

        
 # ADMINISTRADORES
class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'


# ESTUDIANTES
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        

# HABILITACIÓN DE MATRÍCULA /
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
        
    def validate_enrollment_end_date(self, value):
        # Verificar que la fecha de fin no sea en el pasado
        if value and value < timezone.now():
            raise serializers.ValidationError("La fecha de fin no puede ser en el pasado.")
        return value
   

#################    MÉTODOS DE PAGO  ########################
class Payment_MethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Methods
        fields = '__all__'


#################     PAGO / PAYMENT   #######################
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        
###############      MODALIDAD DE CURSOS   ##################  
class CourseModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModality
        fields = '__all__'


#############   TABLA INTERMEDIA  ##########
class Student_CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Courses
        fields = '__all__'       

########### TABLA INTERMEDIA   #############
class Student_PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Payments
        fields = '__all__'       
        
#########   Eventos ################
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'