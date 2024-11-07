import requests
import unittest

class TestAPIStatusCode(unittest.TestCase):

    def test_get_status_code(self):
        # Step 1: Make a GET request to the demo API
        url = "https://reqres.in/api/users/2"  # Example URL from ReqRes
        response = requests.get(url)
        
        # Step 2: Validate whether the response code is 200
        self.assertEqual(response.status_code, 200, f"Expected status code 200, but got {response.status_code}")
        
        # Optionally: Print the response to inspect further details (for debugging)
        print(f"Response Code: {response.status_code}")
        print(f"Response Body: {response.json()}")

# To run the test if this script is executed directly
if __name__ == "__main__":
    unittest.main()
