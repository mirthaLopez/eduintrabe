from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from .models import (
    Partners, Courses_Category, Payment_Modality,  Courses, People_Interested, Provinces, Cantons, Districts, 
    Neighborhoods, Genre, Student_Status, Identifications, Form, Administrator, Student, Enrollment, 
    Payment_Methods, Payment, CourseModality, Student_Courses, Student_Payments, Event, Blog
    )

from .serializers import (
    UserAdminRegisterSerializer, UserStudentRegisterSerializer,PartnersSerializer, PaymentModalitySerializer, 
    Courses_CategorySerializer, CoursesSerializer, People_InterestedSerializer, ProvincesSerializer, 
    CantonsSerializer, DistrictsSerializer, NeighborhoodsSerializer, GenreSerializer, Student_StatusSerializer, 
    IdentificationsSerializer, FormSerializer, AdministratorSerializer, StudentSerializer, EnrollmentSerializer, 
    Payment_MethodsSerializer, PaymentSerializer, CourseModalitySerializer, Student_CoursesSerializer, Student_PaymentSerializer, EventSerializer, BlogSerializer
)


"""
permission_classes = [IsAuthenticated, IsAdmin]
permission_classes = [IsAuthenticated, IsAdmin | IsStudent]
"""

#SE ESTABLECEN LOS ROLES, QUE FUERON ESTABLECIDOS EN LA INTERFAZ DE ADMIN DJANGO

#ADMINISTRACIÓN
class IsAdmin(BasePermission): 
    # Permiso para verificar si el usuario pertenece al grupo "Admin"
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Admin").exists()
   
#ESTUDIANTE
class IsStudent(BasePermission):
    # Permiso para verificar si el usuario pertenece al grupo "Student"
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Student").exists()
    
#######################################################################################

class UserAdminListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAdminRegisterSerializer

class UserAdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserAdminRegisterSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Usuario eliminado exitosamente'}, status=status.HTTP_204_NO_CONTENT)

#######################################################################################

class UserStudentListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserStudentRegisterSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
   
class UserStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserStudentRegisterSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsStudent]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Categoría de menú eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)


class EmailTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            raise AuthenticationFailed('El email y la contraseña son obligatorios.')

        try:
            # Intentamos obtener el usuario con el correo electrónico
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed('Usuario no encontrado.')

        # Autenticamos con el correo y la contraseña
        user = authenticate(username=user.username, password=password)  # authenticate usa el 'username', pero hemos obtenido el 'email'

        if not user:
            raise AuthenticationFailed('Credenciales incorrectas.')

        # Generamos los tokens JWT
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        })

class PartnersListView(generics.ListCreateAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [AllowAny]

class PartnersCreateView(generics.CreateAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
class PartnersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class PaymentModalityListCreateView(generics.ListCreateAPIView):
    queryset = Payment_Modality.objects.all()
    serializer_class = PaymentModalitySerializer

class PaymentModalityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment_Modality.objects.all()
    serializer_class = PaymentModalitySerializer
    permission_classes = [IsAuthenticated, IsAdmin]
   
class Courses_CategoryListCreate(generics.ListCreateAPIView):
    queryset = Courses_Category.objects.all()
    serializer_class = Courses_CategorySerializer
    permission_classes = [AllowAny]
    

class Courses_CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses_Category.objects.all()
    serializer_class = Courses_CategorySerializer
    permission_classes = [AllowAny]

    
class CoursesList(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [AllowAny]

class CoursesCreateView(generics.CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class CoursesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class People_InterestedListCreate(generics.ListCreateAPIView):
    queryset = People_Interested.objects.all()
    serializer_class = People_InterestedSerializer

class People_InterestedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = People_Interested.objects.all()
    serializer_class = People_InterestedSerializer

class ProvincesListCreate(generics.ListCreateAPIView):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer

class ProvincesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer

class CantonsListCreate(generics.ListCreateAPIView):
    queryset = Cantons.objects.all()
    serializer_class = CantonsSerializer

class CantonsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cantons.objects.all()
    serializer_class = CantonsSerializer

class DistrictsListCreate(generics.ListCreateAPIView):
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer

class DistrictsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer

class NeighborhoodsListCreate(generics.ListCreateAPIView):
    queryset = Neighborhoods.objects.all()
    serializer_class = NeighborhoodsSerializer

class NeighborhoodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Neighborhoods.objects.all()
    serializer_class = NeighborhoodsSerializer

class GenreListCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class Student_StatusListCreate(generics.ListCreateAPIView):
    queryset = Student_Status.objects.all()
    serializer_class = Student_StatusSerializer

class Student_StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student_Status.objects.all()
    serializer_class = Student_StatusSerializer

class IdentificationsListCreate(generics.ListCreateAPIView):
    queryset = Identifications.objects.all()
    serializer_class = IdentificationsSerializer

class IdentificationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Identifications.objects.all()
    serializer_class = IdentificationsSerializer

class FormListCreate(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [AllowAny] 


class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [AllowAny] 

class AdministratorListCreate(generics.ListCreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

class AdministratorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentCreateView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class EnrollmentListView(generics.ListAPIView):
    queryset = Enrollment.objects.all()  
    serializer_class = EnrollmentSerializer 
    permission_classes = [AllowAny] 

class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class Payment_MethodsListCreate(generics.ListCreateAPIView):
    queryset = Payment_Methods.objects.all()
    serializer_class = Payment_MethodsSerializer
    permission_classes = [AllowAny]

class Payment_MethodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment_Methods.objects.all()
    serializer_class = Payment_MethodsSerializer
    permission_classes = [AllowAny]

class PaymentListCreate(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]

class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]


class CourseModalityListCreateView(generics.ListCreateAPIView):
    queryset = CourseModality.objects.all()
    serializer_class = CourseModalitySerializer

class CourseModalityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseModality.objects.all()
    serializer_class = CourseModalitySerializer


class Student_CoursesListCreateView(generics.ListCreateAPIView):
    queryset = Student_Courses.objects.all()
    serializer_class = Student_CoursesSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsStudent]

class Student_CoursesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student_Courses.objects.all()
    serializer_class = Student_CoursesSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsStudent]


class Student_PaymentsListCreateView(generics.ListCreateAPIView):
    queryset = Student_Payments.objects.all()
    serializer_class = Student_PaymentSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsStudent]

class Student_PaymentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student_Payments.objects.all()
    serializer_class = Student_PaymentSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsStudent]
    

class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    

class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Vista para obtener, actualizar y eliminar un blog específico
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]