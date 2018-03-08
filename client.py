import requests


r1 = requests.get("http://vcm-3574.vm.duke.edu:5000/name")
print(r1.json())


r2 = requests.get("http://vcm-3574.vm.duke.edu:5000/hello/human")
print(r2.json())

d = {
    "a": [2, 4],
    "b": [5, 6]
}
r3 = requests.post("http://vcm-3574.vm.duke.edu:5000/distance", json=d)
print(r3.json())
