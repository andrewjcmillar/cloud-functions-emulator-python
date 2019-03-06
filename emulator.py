import click
from flask import Flask, request


@click.command()
@click.argument('function_name')
@click.option('--route', default='/', help='Route to deploy function to')
@click.option('--port', default=3001, help='Port to deploy function on')
def emulator(function_name, route, port):
    app = Flask(__name__)
    function = getattr(__import__('main', fromlist=[function_name]), function_name)
    new_func = _add_request(function)
    app.add_url_rule(f'/{route}', view_func=new_func, methods=['GET', 'POST', 'PUT', 'OPTIONS'])
    app.run(port=port)


def _add_request(function):
    def new_func():
        return function(request)
    return new_func


if __name__ == '__main__':
    emulator()
