import requests
import json
import time
import hashlib
import re
from typing import Dict, Any, List

class WorkingAPITester:
    def __init__(self, base_url: str = "https://blackbox-interface.vercel.app"):
        self.base_url = base_url
        self.session = requests.Session()
        self.results = {}
    
    def test_endpoint(self, endpoint: str, method: str = "POST", data: Dict = None) -> Dict:
        """Test an endpoint and return the response"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method.upper() == "GET":
                response = self.session.get(url)
            else:
                response = self.session.post(url, json=data)
            
            # Handle different response types
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    return {
                        "status_code": response.status_code,
                        "response": response_data,
                        "success": True
                    }
                except json.JSONDecodeError:
                    return {
                        "status_code": response.status_code,
                        "response": {"text": response.text},
                        "success": True
                    }
            else:
                return {
                    "status_code": response.status_code,
                    "response": {"error": response.text},
                    "success": False
                }
        except Exception as e:
            return {
                "status_code": None,
                "response": {"error": str(e)},
                "success": False
            }
    
    def test_data_endpoint(self):
        """Test the /data endpoint with various inputs"""
        print("🔍 Testing /data endpoint...")
        print("-" * 40)
        
        test_cases = [
            "hello", "world", "test", "123", "abc", "", "a", "aa", "aaa",
            "Hello World", "hello world", "HELLO", "hello123", "123hello"
        ]
        
        results = []
        for test_input in test_cases:
            result = self.test_endpoint("/data", data={"data": test_input})
            if result["success"]:
                output = result["response"].get("result")
                print(f"  Input: '{test_input}' → Output: {output}")
                results.append({
                    "input": test_input,
                    "output": output,
                    "status": "success"
                })
            else:
                print(f"  Input: '{test_input}' → Error: {result['response'].get('error')}")
                results.append({
                    "input": test_input,
                    "output": None,
                    "status": "error",
                    "error": result["response"].get("error")
                })
        
        return results
    
    def test_time_endpoint(self):
        """Test the /time endpoint"""
        print("\n⏰ Testing /time endpoint...")
        print("-" * 40)
        
        results = []
        for i in range(3):
            result = self.test_endpoint("/time", method="GET")
            if result["success"]:
                output = result["response"].get("result")
                print(f"  Call {i+1}: {output}")
                results.append({
                    "call": i+1,
                    "output": output,
                    "status": "success"
                })
            else:
                print(f"  Call {i+1}: Error - {result['response'].get('error')}")
                results.append({
                    "call": i+1,
                    "output": None,
                    "status": "error",
                    "error": result["response"].get("error")
                })
            time.sleep(1)
        
        return results
    
    def test_fizzbuzz_endpoint(self):
        """Test the /fizzbuzz endpoint"""
        print("\n🎯 Testing /fizzbuzz endpoint...")
        print("-" * 40)
        
        test_cases = [
            "1", "2", "3", "4", "5", "15", "30", "45", "60", "75", "90", "105",
            "hello", "world", "abc", "123", "15abc", "abc15", "fizz", "buzz", "fizzbuzz"
        ]
        
        results = []
        for test_input in test_cases:
            result = self.test_endpoint("/fizzbuzz", data={"data": test_input})
            if result["success"]:
                output = result["response"].get("result")
                print(f"  Input: '{test_input}' → Output: {output}")
                results.append({
                    "input": test_input,
                    "output": output,
                    "status": "success"
                })
            else:
                print(f"  Input: '{test_input}' → Error: {result['response'].get('error')}")
                results.append({
                    "input": test_input,
                    "output": None,
                    "status": "error",
                    "error": result["response"].get("error")
                })
        
        return results
    
    def test_glitch_endpoint(self):
        """Test the /glitch endpoint"""
        print("\n⚡ Testing /glitch endpoint...")
        print("-" * 40)
        
        test_cases = [
            "hello", "world", "test", "123", "abc", "", "a", "aa", "aaa",
            "glitch", "error", "bug", "fail", "success", "true", "false"
        ]
        
        results = []
        for test_input in test_cases:
            result = self.test_endpoint("/glitch", data={"data": test_input})
            if result["success"]:
                output = result["response"].get("result")
                print(f"  Input: '{test_input}' → Output: {output}")
                results.append({
                    "input": test_input,
                    "output": output,
                    "status": "success"
                })
            else:
                print(f"  Input: '{test_input}' → Error: {result['response'].get('error')}")
                results.append({
                    "input": test_input,
                    "output": None,
                    "status": "error",
                    "error": result["response"].get("error")
                })
        
        return results
    
    def test_zap_endpoint(self):
        """Test the /zap endpoint"""
        print("\n⚡ Testing /zap endpoint...")
        print("-" * 40)
        
        test_cases = [
            "hello", "world", "test", "123", "abc", "", "a", "aa", "aaa",
            "zap", "ZAP", "Zap", "zAp", "zaP", "ZaP", "zAP", "ZAp"
        ]
        
        results = []
        for test_input in test_cases:
            result = self.test_endpoint("/zap", data={"data": test_input})
            if result["success"]:
                output = result["response"].get("result")
                print(f"  Input: '{test_input}' → Output: '{output}'")
                results.append({
                    "input": test_input,
                    "output": output,
                    "status": "success"
                })
            else:
                print(f"  Input: '{test_input}' → Error: {result['response'].get('error')}")
                results.append({
                    "input": test_input,
                    "output": None,
                    "status": "error",
                    "error": result["response"].get("error")
                })
        
        return results
    
    def test_alpha_endpoint(self):
        """Test the /alpha endpoint"""
        print("\n🔤 Testing /alpha endpoint...")
        print("-" * 40)
        
        # Test with various inputs
        test_cases = [
            "hello", "world", "test", "123", "abc", "", "a", "aa", "aaa",
            "alpha", "ALPHA", "Alpha", "aLPHA", "alPHA", "alpHA", "alphA",
            "Hello World", "hello world", "HELLO", "hello123", "123hello",
            "special!@#$%", "unicode: 🚀", "very long string " * 100
        ]
        
        results = []
        for test_input in test_cases:
            result = self.test_endpoint("/alpha", data={"data": test_input})
            if result["success"]:
                output = result["response"].get("result")
                print(f"  Input: '{test_input}' → Output: {output}")
                results.append({
                    "input": test_input,
                    "output": output,
                    "status": "success"
                })
            else:
                print(f"  Input: '{test_input}' → Error: {result['response'].get('error')}")
                results.append({
                    "input": test_input,
                    "output": None,
                    "status": "error",
                    "error": result["response"].get("error")
                })
        
        # Analyze alpha patterns
        self.analyze_alpha_patterns(results)
        return results
    
    def analyze_alpha_patterns(self, results: List[Dict]):
        """Analyze patterns in /alpha endpoint responses"""
        print("\n📊 Analyzing /alpha patterns:")
        
        # Check for alphabetical patterns
        alpha_true = 0
        alpha_false = 0
        non_alpha_true = 0
        non_alpha_false = 0
        
        for result in results:
            if result["status"] == "success" and result["output"] is not None:
                input_str = result["input"]
                if input_str.isalpha():
                    if result["output"] is True:
                        alpha_true += 1
                    else:
                        alpha_false += 1
                else:
                    if result["output"] is True:
                        non_alpha_true += 1
                    else:
                        non_alpha_false += 1
        
        print(f"  Alphabetic strings - True: {alpha_true}, False: {alpha_false}")
        print(f"  Non-alphabetic strings - True: {non_alpha_true}, False: {non_alpha_false}")
        
        # Check for specific patterns
        if alpha_true > 0 and non_alpha_false > 0:
            print("  ✅ Pattern: Returns true for alphabetic strings only")
        else:
            print("  ❓ Pattern not immediately obvious - needs more investigation")
    
    def analyze_patterns(self):
        """Analyze patterns in the collected results"""
        print("\n📊 Pattern Analysis")
        print("=" * 50)
        
        # Analyze /data patterns
        if "data" in self.results:
            print("\n📊 /data endpoint patterns:")
            data_results = [r for r in self.results["data"] if r["status"] == "success"]
            if data_results:
                print(f"  - {len(data_results)} successful responses")
                print(f"  - Output type: {type(data_results[0]['output']).__name__}")
                # Check if it's a hash function
                for result in data_results[:3]:  # Check first 3
                    input_str = result["input"]
                    output = result["output"]
                    print(f"  - '{input_str}' → {output}")
        
        # Analyze /fizzbuzz patterns
        if "fizzbuzz" in self.results:
            print("\n🎯 /fizzbuzz endpoint patterns:")
            fizzbuzz_results = [r for r in self.results["fizzbuzz"] if r["status"] == "success"]
            if fizzbuzz_results:
                true_count = sum(1 for r in fizzbuzz_results if r["output"] is True)
                false_count = sum(1 for r in fizzbuzz_results if r["output"] is False)
                print(f"  - True responses: {true_count}")
                print(f"  - False responses: {false_count}")
                
                # Check for FizzBuzz pattern
                for result in fizzbuzz_results:
                    if result["output"] is True:
                        print(f"  - TRUE for: '{result['input']}'")
        
        # Analyze /zap patterns
        if "zap" in self.results:
            print("\n⚡ /zap endpoint patterns:")
            zap_results = [r for r in self.results["zap"] if r["status"] == "success"]
            if zap_results:
                echo_count = sum(1 for r in zap_results if r["input"] == r["output"])
                print(f"  - Echo responses: {echo_count}/{len(zap_results)}")
                if echo_count == len(zap_results):
                    print("  - ✅ Perfect echo function confirmed!")
        
        # Analyze /glitch patterns
        if "glitch" in self.results:
            print("\n⚡ /glitch endpoint patterns:")
            glitch_results = [r for r in self.results["glitch"] if r["status"] == "success"]
            if glitch_results:
                true_count = sum(1 for r in glitch_results if r["output"] is True)
                false_count = sum(1 for r in glitch_results if r["output"] is False)
                print(f"  - True responses: {true_count}")
                print(f"  - False responses: {false_count}")
                
                # Check for length-based patterns
                for result in glitch_results:
                    if result["output"] is True:
                        print(f"  - TRUE for length {len(result['input'])}: '{result['input']}'")
    
    def run_comprehensive_test(self):
        """Run comprehensive tests on all endpoints"""
        print("🚀 Starting comprehensive API testing...")
        print("=" * 60)
        
        # Test all endpoints
        self.results["data"] = self.test_data_endpoint()
        self.results["time"] = self.test_time_endpoint()
        self.results["fizzbuzz"] = self.test_fizzbuzz_endpoint()
        self.results["glitch"] = self.test_glitch_endpoint()
        self.results["zap"] = self.test_zap_endpoint()
        self.results["alpha"] = self.test_alpha_endpoint()
        
        # Analyze patterns
        self.analyze_patterns()
        
        # Generate summary
        self.generate_summary()
    
    def generate_summary(self):
        """Generate a summary of findings"""
        print("\n📋 Summary of Findings")
        print("=" * 50)
        
        total_endpoints = len(self.results)
        successful_endpoints = sum(1 for endpoint, results in self.results.items() 
                                 if any(r["status"] == "success" for r in results))
        
        print(f"Endpoints tested: {total_endpoints}")
        print(f"Endpoints with successful responses: {successful_endpoints}")
        
        for endpoint, results in self.results.items():
            success_count = sum(1 for r in results if r["status"] == "success")
            error_count = sum(1 for r in results if r["status"] == "error")
            print(f"\n{endpoint}: {success_count} success, {error_count} errors")
            
            if success_count > 0:
                # Show sample successful response
                sample = next(r for r in results if r["status"] == "success")
                print(f"  Sample: '{sample['input']}' → {sample['output']}")

if __name__ == "__main__":
    tester = WorkingAPITester()
    tester.run_comprehensive_test() 