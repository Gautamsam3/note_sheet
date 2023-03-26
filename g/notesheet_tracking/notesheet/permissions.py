from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from .models import ClassCoordinator, HeadOfDepartment, Dean, Notesheet, NotesheetReview

def add_group_permissions(group_name, model_class, permissions):
    """
    Helper function to add permissions to a group for a model class
    """
    content_type = ContentType.objects.get_for_model(model_class)
    group, created = Group.objects.get_or_create(name=group_name)
    for codename, name in permissions:
        permission, created = Permission.objects.get_or_create(
            codename=codename,
            name=name,
            content_type=content_type,
        )
        group.permissions.add(permission)

# Permissions for Student model
add_group_permissions(
    'student',
    Notesheet,
    [
        ('add_notesheet', 'Can add notesheet'),
        ('change_notesheet', 'Can change notesheet'),
    ]
)

# Permissions for ClassCoordinator model
add_group_permissions(
    'class_coordinator',
    Notesheet,
    [
        ('add_notesheet', 'Can add notesheet'),
        ('change_notesheet', 'Can change notesheet'),
        ('delete_notesheet', 'Can delete notesheet'),
    ]
)
add_group_permissions(
    'class_coordinator',
    NotesheetReview,
    [
        ('change_notesheetreview', 'Can change notesheet review'),
    ]
)

# Permissions for HeadOfDepartment model
add_group_permissions(
    'head_of_department',
    Notesheet,
    [
        ('add_notesheet', 'Can add notesheet'),
        ('change_notesheet', 'Can change notesheet'),
        ('delete_notesheet', 'Can delete notesheet'),
    ]
)
add_group_permissions(
    'head_of_department',
    NotesheetReview,
    [
        ('change_notesheetreview', 'Can change notesheet review'),
    ]
)

# Permissions for Dean model
add_group_permissions(
    'dean',
    Notesheet,
    [
        ('add_notesheet', 'Can add notesheet'),
        ('change_notesheet', 'Can change notesheet'),
        ('delete_notesheet', 'Can delete notesheet'),
    ]
)
add_group_permissions(
    'dean',
    NotesheetReview,
    [
        ('change_notesheetreview', 'Can change notesheet review'),
    ]
)
