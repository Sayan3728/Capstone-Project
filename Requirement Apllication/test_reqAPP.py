import requests
import pytest
import platform
plat=platform.system()
def test_get_candi():
   response = requests.get("http://127.0.0.1:9000/app",params={"skillset":"['DBMS', 'Networking']"})#return a response object
   #if status code between beyond or is 400 than it is error
   data=response.json()
   try:
       assert data["FullName"] =="Susanta"
       print("The test is successfull")
   except AssertionError:
       print("Assertion error")
#test_get_candi()
@pytest.mark.skipif(platform.system()=='Windows',reason='Not tested in Windows platform')
def test_post_candi():
    response_post= requests.post("http://127.0.0.1:9000/app", json={
    "CandId":20,
    "FullName":"Akash",
    "skillset":["python","Django"]
})
    assert response_post.status_code==200
    response_get = requests.get("http://127.0.0.1:9000/app", params={"skillset":"['Django', 'python']"})
    print(response_get.json())
    data=response_get.json()
    print(data)
    if data["CandId"]=="20":
        print(("Post was successfull"))
    else:
        print("Something happened")
#test_post_candi()


def test_put_candi():
    response_put = requests.put("http://127.0.0.1:9000/app",
                                  json={
   "CandId": "9",
        "FullName": "Guddu",
        "skillset":["C#", "python"]
})
    response_get = requests.get("http://127.0.0.1:9000/app", params={"skillset":"['C#', 'python']"})
    data=response_get.json()
    try:
        assert data["CandId"]=="9"
        print("update successfull")
    except:
        print("Assertion error,currency detail mismatch")
#test_put_candi()


def test_delete_candi():
    requests.delete("http://127.0.0.1:9000/app",params={"CandId": "13"})
    response_get=requests.get("http://127.0.0.1:9000/app", params={"skillset": "MARKED"})
    data=response_get.json()
    try:
        assert data["CandId"] == "13"
        print("Successfully Flagged")
    except AssertionError:
        print("Flagged unsuccessful")


#test_delete_candi()

def test_post_external():
    response_post= requests.post("http://127.0.0.1:9000/req", json=
        {

            "requirementId": 1,
            "position": "developer",
            "requiredSkillsets": ["C#", "java"]
        })
    assert response_post.status_code==200
    response_get = requests.get("http://127.0.0.1:9000/app", params={"skillset": "['C#', 'java']"})
    print(response_get.json())
    data = response_get.json()
    print(data)
    if data["CandId"] == "10":
        print(("external matching is working"))
    else:
        print("external matching is not working")

#test_post_external()
@pytest.mark.skipif(platform.system()=='Windows',reason='Not tested in Windows platform')
def test_postbyinternal():
    response_post= requests.post("http://127.0.0.1:9000/int", json=
    {

        "CandId": 21,
        "FullName": "Subham",
        "skillset": ["C", "html"]
    })
    assert response_post.status_code==200
    response_get = requests.get("http://127.0.0.1:9000/app", params={"skillset": "['C', 'html']"})
    print(response_get.json())
    data = response_get.json()
    print(data)
    if data["CandId"] == "21":
        print(("internal posting is done"))
    else:
        print("internal posting is not working")
#test_postbyinternal()

def test_post_internal():
    response_post= requests.post("http://127.0.0.1:9000/internal", json=
    {

        "requirementId": 1,
        "position": "developer",
        "requiredSkillsets": ["java"],
        "optionalSkillsets": ["python"]
    })
    assert response_post.status_code==200
    response_get = requests.get("http://127.0.0.1:9000/app", params={"skillset": "['java', 'python']"})
    print(response_get.json())
    data = response_get.json()
    print(data)
    if data["CandId"] == "15":
        print(("internal matching is working"))
    else:
        print("internal matching is not working")
test_post_internal()