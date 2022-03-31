from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from .consumers import GraphConsumer

ws_urlpatterns = [
    path('ws/graph/', GraphConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
