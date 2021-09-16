import secrets

import docker
from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from fastapi import status

from credentials import TOKEN

docker_client = docker.from_env()
app = FastAPI()


def get_active_containers():
    return [
        {
            'short_id': container.short_id,
            'container_name': container.name,
            'image_name': container.image.tags,
            'created': container.attrs['Created'],
            'status': container.status,
            'ports': container.ports,
        }
        for container in docker_client.containers.list()
    ]


def stop_container(container_name: str) -> bool:
    try:
        docker_client.containers.get(container_name).stop()
    except Exception as e:
        print(f'Error while delete container {container_name}, {e}')
        return False
    print(f'Container deleted. container_name = {container_name}')
    return True


def deploy_new_container(image_name: str, container_name: str, ports: dict = None):

    try:
        print(f'pull {image_name}, name={container_name}')
        docker_client.images.pull(image_name)
        print('success')
        stop_container(container_name)
        print('old stopped')
        docker_client.containers.run(image=image_name, name=container_name, detach=True, ports=ports)
    except Exception as e:
        print(f'Error while deploy container {container_name}, \n{e}')
        return {'status': 'error', 'exception': str(e)}
    print(f'container deployed. container_name = {container_name}')
    return {'status': 'success'}


@app.get('/')
async def list_containers(token=Header(None)):
    if not secrets.compare_digest(token, TOKEN):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='access denied: invalid token')
    return get_active_containers()


@app.post('/')
async def deploy_container(token=Header(None)):
    """
    example body:
    {
        'username': 'admin',
        'repository': 'hello_world',
        'tag': '0.0.1',
        'ports': {8080': 8080, 443: 443},
    }
    """
    if not secrets.compare_digest(token, TOKEN):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail='access denied: invalid token')
    # return deploy_new_container()
    return {'status': 'not_implemented'}
