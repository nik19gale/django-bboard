from .models import Category, Advertisement

def navigator(request):
    return {
        'navigator': {
            'categories': Category.objects.all()
        }
    }