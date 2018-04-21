from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from .models import Example


@csrf_exempt
def example_list(request):
  if request.method == "GET":
    examples = Example.objects.all()
    examples_json = [t.to_json() for t in examples]
    return JsonResponse(examples_json, safe=False)
  elif request.method == "POST":
    data = request.POST
    example = Test()
    example.title = data.get('title', '')
    example.text = data.get('text', '')
    example.save()
    
    return JsonResponse( example.to_json(), status=201)


@csrf_exempt
def example_detail(request, test_id):

  try:
    example = Example.objects.get(pk= example_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    return JsonResponse(example.to_json())
  elif request.method == "PUT":
    data = QueryDict(request.body)
    example.title = data.get('title', example.title)
    example.body = data.get('text', example.text)
    example.save()
    return JsonResponse(example.to_json())
  elif request.method == "DELETE":
    example.delete()
    return JsonResponse(example.to_json())