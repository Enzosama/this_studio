from collections.abc import Callable

from django.http.request import HttpRequest
from django.utils.safestring import SafeText

def csrf_input(request: HttpRequest) -> SafeText: ...

csrf_input_lazy: Callable[[HttpRequest], SafeText]
csrf_token_lazy: Callable[[HttpRequest], SafeText]
