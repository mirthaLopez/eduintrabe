from django.db import models
from django.contrib.auth.models import User

#Primera migracion
class Partners(models.Model):
    partner_name = models.CharField(max_length=100)
    partner_logo_url = models.URLField()

# Segunda migracion
class Courses_Category(models.Model):
    category_name = models.CharField(max_length=100)
    
class Payment_Modality(models.Model):
    payment_modality_name = models.CharField(max_length=100, unique=True)

#Tercera migracio
class Courses(models.Model):
    course_image_url = models.URLField()
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    course_price = models.DecimalField(max_digits=10, decimal_places=2)
    course_schedule = models.CharField(max_length=40)
    begins = models.DateField()
    ends = models.DateField()
    course_duration =  models.CharField(max_length=30)
    is_free=models.BooleanField(null=True)
    obligatory_requirements=models.TextField(null=True)
    course_category_fk = models.ForeignKey(Courses_Category, on_delete=models.CASCADE)
    payment_modality_fk= models.ForeignKey(Payment_Modality, on_delete=models.CASCADE, null=True)

#Cuarta migracion 
class People_Interested(models.Model):
    person_name = models.CharField(max_length=50)
    person_first_last_name = models.CharField(max_length=50)
    person_email = models.EmailField()
    person_phone_number = models.CharField(max_length=20)
    person_notes = models.TextField(max_length=255)
    course = models.TextField(max_length=50)
    
#Quinta migracion 
class Provinces(models.Model):
    province_name = models.CharField(max_length=50)

class Cantons(models.Model):
    canton_name = models.CharField(max_length=100)
    province_fk = models.ForeignKey(Provinces, on_delete=models.CASCADE)
   
class Districts(models.Model):
    district_name = models.CharField(max_length=100)
    canton_fk = models.ForeignKey(Cantons, on_delete=models.CASCADE)
   
class Neighborhoods(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    district_fk =  models.ForeignKey(Districts, on_delete=models.CASCADE)

#Sexta migracion 
class Genre(models.Model):
    genre_name = models.CharField(max_length=50)

#Sétima migración 
class Student_Status(models.Model):
    status_name = models.CharField(max_length=50)

#Octava migración 
class Identifications(models.Model):
    identification_type = models.CharField(max_length=50)
    
#Catorceava migración 
class Payment_Methods(models.Model):
    payment_method_name = models.CharField(max_length=50)

#Quincea migración 
class Payment(models.Model):
    payment_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_receipt_url = models.URLField(null=True, blank=True)
    payment_receipt_number = models.CharField(max_length=50, null=True, blank=True)
    payment_method_fk = models.ForeignKey(Payment_Methods, on_delete=models.CASCADE)
    
#Novena migración 
class Form(models.Model):
    identification_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    first_last_name = models.CharField(max_length=50)
    second_last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    identification_fk = models.ForeignKey(Identifications, on_delete=models.CASCADE)
    genre_fk =  models.ForeignKey(Genre, on_delete=models.CASCADE)
    course_fk = models.ForeignKey(Courses, on_delete=models.CASCADE)
    student_status_fk = models.ForeignKey(Student_Status, on_delete=models.CASCADE)
    identification_image_url = models.URLField(null=True)
    address = models.TextField(null=True)
    neighborhood_fk = models.ForeignKey(Neighborhoods, on_delete=models.CASCADE , null=True)
    payment_fk= models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)

#Decima migración 
class Administrator(models.Model):  
    admin_name = models.CharField(max_length=50)
    admin_first_last_name = models.CharField(max_length=50)
    admin_second_last_name = models.CharField(max_length=50)
    admin_phone_number = models.CharField(max_length=20)
    admin_email = models.EmailField()
    admin_auth_user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    
#Undecima migración 
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_first_last_name = models.CharField(max_length=50)
    student_second_last_name = models.CharField(max_length=50)
    student_birth_date = models.DateField()
    student_phone_number = models.CharField(max_length=20)
    student_email = models.EmailField()
    student_id_url= models.URLField(null=True)
    student_auth_user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    identification_number = models.CharField(max_length=50, unique=True, null=True)
    identification_fk = models.ForeignKey(Identifications, on_delete=models.CASCADE, null=True)
    genre_fk =  models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    address = models.TextField(null=True)
    neighborhood_fk = models.ForeignKey(Neighborhoods, on_delete=models.CASCADE, null=True)


class CourseModality(models.Model):
    modality_name = models.CharField(max_length=50)

#Treceava migración 
class Enrollment(models.Model):
    enrollment_start_date = models.DateTimeField(null=True)
    enrollment_end_date = models.DateTimeField(null=True)
    available_spots=models.IntegerField(null=True)
    course_fk = models.ForeignKey(Courses, on_delete=models.CASCADE)
    course_modality_fk= models.ForeignKey(CourseModality, on_delete=models.CASCADE, null=True)

class Student_Courses(models.Model):
    course_fk= models.ForeignKey(Courses, on_delete=models.CASCADE)
    student_fk= models.ForeignKey(Student, on_delete=models.CASCADE)
    
    
class Student_Payments(models.Model):
    student_fk= models.ForeignKey(Student, on_delete=models.CASCADE)
    payment_fk= models.ForeignKey(Payment, on_delete=models.CASCADE)

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    description = models.TextField(max_length=255)

class Blog(models.Model):
    title = models.CharField(max_length=100)  # Título del blog
    creator = models.CharField(max_length=50)  # Nombre del creador
    introduction = models.CharField(max_length=255)  # Introducción (máx. 255 caracteres)
    content = models.TextField()  # Contenido del blog
    image_url = models.URLField(max_length=255)  # URL de la imagen
    likes_count = models.IntegerField(default=0)  # Contador de likes