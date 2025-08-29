import requests
import json
import sys

def test_api(base_url="http://localhost:5000"):
    """Test the API with the provided examples"""
    
    test_cases = [
        {
            "name": "Example A",
            "data": ["a", "1", "334", "4", "R", "$"],
            "expected": {
                "odd_numbers": ["1"],
                "even_numbers": ["334", "4"],
                "alphabets": ["A", "R"],
                "special_characters": ["$"],
                "sum": "339",
                "concat_string": "Ra"
            }
        },
        {
            "name": "Example B",
            "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"],
            "expected": {
                "odd_numbers": ["5"],
                "even_numbers": ["2", "4", "92"],
                "alphabets": ["A", "Y", "B"],
                "special_characters": ["&", "-", "*"],
                "sum": "103",
                "concat_string": "ByA"
            }
        },
        {
            "name": "Example C",
            "data": ["A", "ABcD", "DOE"],
            "expected": {
                "odd_numbers": [],
                "even_numbers": [],
                "alphabets": ["A", "ABCD", "DOE"],
                "special_characters": [],
                "sum": "0",
                "concat_string": "EoDdCbAa"
            }
        }
    ]
    
    print("🧪 Testing Array Processing API")
    print("=" * 50)
    
    for test_case in test_cases:
        print(f"\n📋 Testing {test_case['name']}")
        print(f"Input: {test_case['data']}")
        
        try:
            # Make API request
            response = requests.post(
                f"{base_url}/bfhl",
                json={"data": test_case['data']},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                
                if result.get("is_success"):
                    print("✅ Request successful!")
                    
                    # Check each expected field
                    all_passed = True
                    for field, expected_value in test_case['expected'].items():
                        actual_value = result.get(field, [])
                        if actual_value == expected_value:
                            print(f"  ✅ {field}: {actual_value}")
                        else:
                            print(f"  ❌ {field}: expected {expected_value}, got {actual_value}")
                            all_passed = False
                    
                    if all_passed:
                        print(f"  🎉 {test_case['name']} - ALL TESTS PASSED!")
                    else:
                        print(f"  ⚠️  {test_case['name']} - SOME TESTS FAILED!")
                        
                else:
                    print(f"❌ API returned error: {result.get('error', 'Unknown error')}")
                    
            else:
                print(f"❌ HTTP Error: {response.status_code}")
                print(f"Response: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error: {e}")
        except json.JSONDecodeError as e:
            print(f"❌ JSON decode error: {e}")
    
    print("\n" + "=" * 50)
    print("🏁 Testing completed!")

def test_health_endpoint(base_url="http://localhost:5000"):
    """Test the health endpoint"""
    print("\n🏥 Testing Health Endpoint")
    print("-" * 30)
    
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Health check passed: {result}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Health check error: {e}")

if __name__ == "__main__":
    # Use command line argument for base URL if provided
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:5000"
    
    print(f"🌐 Testing API at: {base_url}")
    
    # Test health endpoint first
    test_health_endpoint(base_url)
    
    # Test main API functionality
    test_api(base_url)
