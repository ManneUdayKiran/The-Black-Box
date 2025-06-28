import requests
import json

def test_api_directly():
    """Test the API endpoints directly to see the actual responses"""
    base_url = "https://blackbox-interface.vercel.app"
    
    print("🔍 Testing API endpoints directly...")
    print("=" * 50)
    
    # Test /data endpoint
    print("\n📊 Testing /data endpoint:")
    try:
        response = requests.post(f"{base_url}/data", json={"data": "hello"})
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response Text: {response.text}")
        try:
            print(f"Response JSON: {response.json()}")
        except:
            print("Response is not JSON")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test /time endpoint
    print("\n⏰ Testing /time endpoint:")
    try:
        response = requests.get(f"{base_url}/time")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response Text: {response.text}")
        try:
            print(f"Response JSON: {response.json()}")
        except:
            print("Response is not JSON")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test /fizzbuzz endpoint
    print("\n🎯 Testing /fizzbuzz endpoint:")
    try:
        response = requests.post(f"{base_url}/fizzbuzz", json={"data": "15"})
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response Text: {response.text}")
        try:
            print(f"Response JSON: {response.json()}")
        except:
            print("Response is not JSON")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test /glitch endpoint
    print("\n⚡ Testing /glitch endpoint:")
    try:
        response = requests.post(f"{base_url}/glitch", json={"data": "hello"})
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response Text: {response.text}")
        try:
            print(f"Response JSON: {response.json()}")
        except:
            print("Response is not JSON")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test /zap endpoint
    print("\n⚡ Testing /zap endpoint:")
    try:
        response = requests.post(f"{base_url}/zap", json={"data": "hello"})
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response Text: {response.text}")
        try:
            print(f"Response JSON: {response.json()}")
        except:
            print("Response is not JSON")
    except Exception as e:
        print(f"Error: {e}")

    # Test /alpha endpoint
    print("\n🔤 Testing /alpha endpoint:")
    try:
        response = requests.post(f"{base_url}/alpha", json={"data": "hello"})
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Response Text: {response.text}")
        try:
            print(f"Response JSON: {response.json()}")
        except:
            print("Response is not JSON")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api_directly() 