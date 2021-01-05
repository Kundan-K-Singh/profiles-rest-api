from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """"Alllow users to edit own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to update its own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id    #$HOW???
