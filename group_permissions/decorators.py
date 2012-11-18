from django.http import HttpResponseForbidden

def authorize(permissions):
    if isinstance(permissions, basestring):
        permissions = [permissions]
    def wrapper(func):
        def inner(request, *args, **kw):
            for permission in permissions:
                if not getattr(request.PERMISSIONS, permission):
                    return HttpResponseForbidden()
            return func(request, *args, **kw)
        return inner
    return wrapper
