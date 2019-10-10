from django.db.models import Q
from django.http import Http404
from . import models

def get_visible_from_queryset(user, queryset):
	"""From a queryset, filter out the students which the user can see."""
	if user.is_staff:
		return queryset
	else:
		return queryset.filter(Q(user = user) | Q(assistant__user = user))

def get_visible_students(user, current = True):
	queryset = models.Student.objects
	if current:
		queryset = queryset.filter(semester__active = True)
	return get_visible_from_queryset(user, queryset)

def check_can_view(request, student):
	if not student.can_view_by(request.user):
		raise Http404("%s cannot view %s" %(request.user, student))
def check_taught_by(request, student):
	if not student.is_taught_by(request.user):
		raise Http404("%s cannot edit %s" %(request.user, student))
