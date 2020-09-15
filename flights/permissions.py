from rest_framework.permissions import BasePermission
from datetime import date
from .models import Booking

class IsBooker(BasePermission):
    message='You are not the booker and admin'

    def has_object_permission(self,request,view,obj):
        if request.user.is_staff or request.user==obj.user:
            return True
        else:
            return False

class MoreThanThreeDays(BasePermission):
    message='To late'
    def has_object_permission(self, request, view, obj):
        if (obj.date - date.today()).days >3:
            return True
        return False
