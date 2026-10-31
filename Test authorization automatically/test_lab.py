import importlib.util


def load(path):
    spec = importlib.util.spec_from_file_location("lab", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_vulnerable_leaks():
    client = load("vulnerable/app.py").app.test_client()
    assert client.get("/orders/2", headers={"X-User": "alice"}).status_code == 200


def test_fixed_blocks_and_allows():
    client = load("fixed/app.py").app.test_client()
    assert client.get("/orders/2", headers={"X-User": "alice"}).status_code == 403
    assert client.get("/orders/1", headers={"X-User": "alice"}).status_code == 200
