def test_create_car(client):
    data = {
        "brand":"Honda",
        "name":"Civic",
        "color":"White",
        "power":"450HP",
        "safety_ratings":"5"
    }
    
    response = client.post("/cars/addCar/", json=data)
    assert response.status_code == 201
    
def test_get_car_by_name(client):
    data = "BE800"
    response = client.get(f"/cars/getCars/name/{data}")
    assert response.status_code == 200
    assert response.json()["name"] == data
    
def test_get_cars_by_brand(client):
    data = "Benz" 
    response = client.get(f"/cars/getCars/brand/{data}")
    assert response.status_code == 200
    assert response.json()[0]["brand"] == data
    
def test_update_car_by_power(client):
    data = {
        "brand":"Honda",
        "name":"Civic",
        "color":"White",
        "power":"700HP",
        "safety_ratings":"5"
    }
    power = "700HP"
    
    response = client.put(f"/cars/updateCar/power/{power}", json=data)
    assert response.status_code == 200
    
def test_delete_car_by_name(client):
    name = "BE800"
    response = client.delete(f"/cars/deleteCar/name/{name}")
    assert response.status_code == 200