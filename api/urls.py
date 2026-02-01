from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, MemberViewSet, BorrowRecordViewSet, index

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrow-records', BorrowRecordViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
