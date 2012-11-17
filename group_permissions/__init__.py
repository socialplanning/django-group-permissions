from django.http import HttpResponseForbidden

class LazyPermissions(object):
    def __init__(self, request):
        self.request = request
        self._groups = None

    def __getattr__(self, permission):
        if self.request.user.is_superuser:
            return True
        if self._groups is None:
            self._groups = list(self.request.user.groups.values_list("name", flat=True))
        return permission in self._groups
