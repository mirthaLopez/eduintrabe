from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from . import views

urlpatterns = [
    path('partners/', views.PartnersListView.as_view(), name='partners-list'),  # Listar Partners
    path('partners/create/', views.PartnersCreateView.as_view(), name='partners-create'),  # Crear Partner
    path('partners/<int:pk>/', views.PartnersDetail.as_view(), name='partners-detail'),
    path('courses_category/', views.Courses_CategoryListCreate.as_view(), name='courses_category-list-create'),
    path('courses_category/<int:pk>/', views.Courses_CategoryDetail.as_view(), name='courses_category-detail'),
    path('courses/', views.CoursesList.as_view(), name='courses-list'),
    path('courses/create/', views.CoursesCreateView.as_view(), name='courses-create'),  # Crear Partner

    path('courses/<int:pk>/', views.CoursesDetail.as_view(), name='courses-detail'),
    path('people_interested/', views.People_InterestedListCreate.as_view(), name='people_interested-list-create'),
    path('people_interested/<int:pk>/', views.People_InterestedDetail.as_view(), name='people_interested-detail'),
    path('provinces/', views.ProvincesListCreate.as_view(), name='provinces-list-create'),
    path('provinces/<int:pk>/', views.ProvincesDetail.as_view(), name='provinces-detail'),
    path('cantons/', views.CantonsListCreate.as_view(), name='cantons-list-create'),
    path('cantons/<int:pk>/', views.CantonsDetail.as_view(), name='cantons-detail'),
    path('districts/', views.DistrictsListCreate.as_view(), name='districts-list-create'),
    path('districts/<int:pk>/', views.DistrictsDetail.as_view(), name='districts-detail'),
    path('neighborhoods/', views.NeighborhoodsListCreate.as_view(), name='neighborhoods-list-create'),
    path('neighborhoods/<int:pk>/', views.NeighborhoodsDetail.as_view(), name='neighborhoods-detail'),
    path('genre/', views.GenreListCreate.as_view(), name='genre-list-create'),
    path('genre/<int:pk>/', views.GenreDetail.as_view(), name='genre-detail'),
    path('student_status/', views.Student_StatusListCreate.as_view(), name='student_status-list-create'),
    path('student_status/<int:pk>/', views.Student_StatusDetail.as_view(), name='student_status-detail'),
    path('identifications/', views.IdentificationsListCreate.as_view(), name='identifications-list-create'),
    path('identifications/<int:pk>/', views.IdentificationsDetail.as_view(), name='identifications-detail'),
    path('form/', views.FormListCreate.as_view(), name='form-list-create'),
    path('form/<int:pk>/', views.FormDetail.as_view(), name='form-detail'),
    path('administrator/', views.AdministratorListCreate.as_view(), name='administrator-list-create'),
    path('administrator/<int:pk>/', views.AdministratorDetail.as_view(), name='administrator-detail'),
    path('student/', views.StudentListCreate.as_view(), name='student-list-create'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
    path('enrollments/', views.EnrollmentListView.as_view(), name='enrollment-list'),  # GET
    path('enrollment/create/', views.EnrollmentCreateView.as_view(), name='enrollment-create'),  # POST
    path('enrollment/<int:pk>/', views.EnrollmentDetail.as_view(), name='enrollment-detail'),
    path('payment_methods/', views.Payment_MethodsListCreate.as_view(), name='payment_methods-list-create'),
    path('payment_methods/<int:pk>/', views.Payment_MethodsDetail.as_view(), name='payment_methods-detail'),
    path('payment/', views.PaymentListCreate.as_view(), name='payment-list-create'),
    path('payment/<int:pk>/', views.PaymentDetail.as_view(), name='payment-detail'),
    path('modalities/', views.CourseModalityListCreateView.as_view(), name='course_modality_list_create'),
    path('modalities/<int:pk>/', views.CourseModalityDetailView.as_view(), name='course_modality_detail'),
    path('payment_modality/', views.PaymentModalityListCreateView.as_view(), name='payment-modality-list-create'),  
    path('payment_modality/<int:pk>/', views.PaymentModalityDetailView.as_view(), name='payment-modality-detail'), 
    path('events/', views.EventListCreate.as_view(), name='event-list-create'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name='event-detail'),
    path('blogs/', views.BlogListCreate.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
    
    # url de tabla intermedia ESTUDIANTE - CURSO
    path('student_courses/', views.Student_CoursesListCreateView.as_view(), name='student-courses-list-create'),  
    path('student_courses/<int:pk>/', views.Student_CoursesDetailView.as_view(), name='student-courses-detail'),

    # url de tabla intermedia ESTUDIANTE -  PAGO
    path('student_payment/', views.Student_PaymentsListCreateView.as_view(), name='student-payment-list-create'),  
    path('student_payment/<int:pk>/', views.Student_PaymentsDetailView.as_view(), name='student-payment-detail'),
  
   # Urls simplejwt token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para obtener token de acceso y refresco
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para refrescar el token de acceso
    path('token/email/', views.EmailTokenObtainPairView.as_view(), name='email_token_obtain_pair'),

    path('users_admin/', views.UserAdminListCreate.as_view(), name='user-list-create'),  
    path('users_admin/<int:pk>/', views.UserAdminDetail.as_view(), name='user-detail'), 
    path('users_student/', views.UserStudentListCreate.as_view(), name='user-list-create'),  
    path('users_student/<int:pk>/', views.UserStudentDetail.as_view(), name='user-detail'), 
]



