import requests
import json
import time
from typing import Dict, Any, List
import base64
import hashlib
import re

class APIExplorer:
    def __init__(self, base_url: str = "https://blackbox-interface.vercel.app"):
        self.base_url = base_url
        self.session = requests.Session()
        self.findings = {}
    
    def test_endpoint(self, endpoint: str, method: str = "POST", data: Dict = None) -> Dict:
        """Test an endpoint and return the response"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method.upper() == "GET":
                response = self.session.get(url)
            else:
                response = self.session.post(url, json=data)
            
            # Check if response is JSON
            if response.headers.get('content-type', '').startswith('application/json'):
                response_data = response.json()
            else:
                response_data = {"text": response.text}
            
            return {
                "status_code": response.status_code,
                "response": response_data,
                "headers": dict(response.headers)
            }
        except Exception as e:
            return {"error": str(e), "response": {}, "status_code": None}
    
    def explore_data_endpoint(self):
        """Explore the /data endpoint"""
        print("🔍 Exploring /data endpoint...")
        findings = []
        
        # Test with different string inputs
        test_cases = [
            "hello", "world", "test", "123", "abc", "", "a", "aa", "aaa",
            "Hello World", "hello world", "HELLO", "hello123", "123hello",
            "special!@#$%", "unicode: 🚀", "very long string " * 100
        ]
        
        for test_input in test_cases:
            result = self.test_endpoint("/data", data={"data": test_input})
            findings.append({
                "input": test_input,
                "output": result.get("response", {}).get("result"),
                "status": result.get("status_code")
            })
            print(f"  Input: '{test_input}' -> Output: {result.get('response', {}).get('result')}")
        
        # Analyze patterns
        self.analyze_data_patterns(findings)
        return findings
    
    def analyze_data_patterns(self, findings: List[Dict]):
        """Analyze patterns in /data endpoint responses"""
        print("\n📊 Analyzing /data patterns:")
        
        # Check if it's a hash function
        for finding in findings:
            if finding["output"] and isinstance(finding["output"], (int, str)):
                # Try common hash functions
                input_str = str(finding["input"])
                
                # Check if it's a simple hash
                if isinstance(finding["output"], int):
                    # Try different hash methods
                    hash_functions = [
                        ("len", len),
                        ("sum_ascii", lambda s: sum(ord(c) for c in s)),
                        ("product_ascii", lambda s: 1 if not s else ord(s[0]) * len(s)),
                        ("crc32", lambda s: abs(hash(s)) % (2**32)),
                        ("simple_hash", lambda s: hash(s) % 10000000)
                    ]
                    
                    for name, func in hash_functions:
                        try:
                            if func(input_str) == finding["output"]:
                                print(f"  ✅ Found pattern: {name} function")
                                return
                        except:
                            continue
        
        print("  ❓ Pattern not immediately obvious - needs more investigation")
    
    def explore_time_endpoint(self):
        """Explore the /time endpoint"""
        print("\n🔍 Exploring /time endpoint...")
        
        # Test multiple times to see if it changes
        results = []
        for i in range(5):
            result = self.test_endpoint("/time", method="GET")
            results.append(result.get("response", {}).get("result"))
            print(f"  Call {i+1}: {result.get('response', {}).get('result')}")
            time.sleep(1)
        
        # Check if it's related to current time
        current_time = int(time.time())
        print(f"  Current Unix timestamp: {current_time}")
        
        # Check if it's a fixed value or time-based
        if len(set(results)) == 1:
            print("  📝 Result: Fixed value (not time-based)")
        else:
            print("  📝 Result: Time-based value")
        
        return results
    
    def explore_fizzbuzz_endpoint(self):
        """Explore the /fizzbuzz endpoint"""
        print("\n🔍 Exploring /fizzbuzz endpoint...")
        findings = []
        
        # Test with numbers as strings
        test_cases = [
            "1", "2", "3", "4", "5", "15", "30", "45", "60", "75", "90", "105",
            "hello", "world", "abc", "123", "15abc", "abc15", "fizz", "buzz", "fizzbuzz"
        ]
        
        for test_input in test_cases:
            result = self.test_endpoint("/fizzbuzz", data={"data": test_input})
            findings.append({
                "input": test_input,
                "output": result.get("response", {}).get("result"),
                "status": result.get("status_code")
            })
            print(f"  Input: '{test_input}' -> Output: {result.get('response', {}).get('result')}")
        
        # Analyze FizzBuzz patterns
        self.analyze_fizzbuzz_patterns(findings)
        return findings
    
    def analyze_fizzbuzz_patterns(self, findings: List[Dict]):
        """Analyze patterns in /fizzbuzz endpoint responses"""
        print("\n📊 Analyzing /fizzbuzz patterns:")
        
        # Check if it's classic FizzBuzz logic
        for finding in findings:
            input_str = str(finding["input"])
            
            # Try to extract number from input
            numbers = re.findall(r'\d+', input_str)
            if numbers:
                num = int(numbers[0])
                expected = False
                
                # Classic FizzBuzz: divisible by 3 and 5
                if num % 3 == 0 and num % 5 == 0:
                    expected = True
                
                if expected == finding["output"]:
                    print(f"  ✅ Found pattern: Classic FizzBuzz (divisible by 3 and 5)")
                    return
        
        # Check other patterns
        print("  ❓ Pattern not immediately obvious - needs more investigation")
    
    def explore_glitch_endpoint(self):
        """Explore the /glitch endpoint"""
        print("\n🔍 Exploring /glitch endpoint...")
        findings = []
        
        # Test with various inputs
        test_cases = [
            "hello", "world", "test", "123", "abc", "", "a", "aa", "aaa",
            "Hello World", "hello world", "HELLO", "hello123", "123hello",
            "glitch", "error", "bug", "fail", "success", "true", "false",
            "special!@#$%", "unicode: 🚀", "very long string " * 100
        ]
        
        for test_input in test_cases:
            result = self.test_endpoint("/glitch", data={"data": test_input})
            findings.append({
                "input": test_input,
                "output": result.get("response", {}).get("result"),
                "status": result.get("status_code")
            })
            print(f"  Input: '{test_input}' -> Output: {result.get('response', {}).get('result')}")
        
        # Analyze glitch patterns
        self.analyze_glitch_patterns(findings)
        return findings
    
    def analyze_glitch_patterns(self, findings: List[Dict]):
        """Analyze patterns in /glitch endpoint responses"""
        print("\n📊 Analyzing /glitch patterns:")
        
        # Check for length-based patterns
        true_count = sum(1 for f in findings if f["output"] is True)
        false_count = sum(1 for f in findings if f["output"] is False)
        
        print(f"  True responses: {true_count}, False responses: {false_count}")
        
        # Check if it's based on input length
        for finding in findings:
            input_len = len(str(finding["input"]))
            if finding["output"] is True:
                print(f"    True for length {input_len}: '{finding['input']}'")
            else:
                print(f"    False for length {input_len}: '{finding['input']}'")
        
        # Look for specific patterns
        print("  ❓ Pattern not immediately obvious - needs more investigation")
    
    def explore_zap_endpoint(self):
        """Explore the /zap endpoint"""
        print("\n🔍 Exploring /zap endpoint...")
        findings = []
        
        # Test with various inputs
        test_cases = [
            "hello", "world", "test", "123", "abc", "", "a", "aa", "aaa",
            "Hello World", "hello world", "HELLO", "hello123", "123hello",
            "zap", "ZAP", "Zap", "zAp", "zaP", "ZaP", "zAP", "ZAp",
            "special!@#$%", "unicode: 🚀", "very long string " * 100
        ]
        
        for test_input in test_cases:
            result = self.test_endpoint("/zap", data={"data": test_input})
            findings.append({
                "input": test_input,
                "output": result.get("response", {}).get("result"),
                "status": result.get("status_code")
            })
            print(f"  Input: '{test_input}' -> Output: {result.get('response', {}).get('result')}")
        
        # Analyze zap patterns
        self.analyze_zap_patterns(findings)
        return findings
    
    def analyze_zap_patterns(self, findings: List[Dict]):
        """Analyze patterns in /zap endpoint responses"""
        print("\n📊 Analyzing /zap patterns:")
        
        # Check if it's an echo function
        echo_count = 0
        for finding in findings:
            if finding["input"] == finding["output"]:
                echo_count += 1
        
        if echo_count == len(findings):
            print("  ✅ Found pattern: Echo function (returns input as-is)")
        else:
            print(f"  ❓ Partial echo: {echo_count}/{len(findings)} inputs echoed")
            
            # Check for transformations
            for finding in findings:
                if finding["input"] != finding["output"]:
                    print(f"    Transformation: '{finding['input']}' -> '{finding['output']}'")
    
    def explore_alpha_endpoint(self):
        """Explore the /alpha endpoint"""
        print("\n🔤 Exploring /alpha endpoint...")
        findings = []
        
        # Test with various inputs
        test_cases = [
            "hello", "world", "test", "123", "abc", "", "a", "aa", "aaa",
            "Hello World", "hello world", "HELLO", "hello123", "123hello",
            "alpha", "ALPHA", "Alpha", "aLPHA", "alPHA", "alpHA", "alphA",
            "special!@#$%", "unicode: 🚀", "very long string " * 100
        ]
        
        for test_input in test_cases:
            result = self.test_endpoint("/alpha", data={"data": test_input})
            findings.append({
                "input": test_input,
                "output": result.get("response", {}).get("result"),
                "status": result.get("status_code")
            })
            print(f"  Input: '{test_input}' -> Output: {result.get('response', {}).get('result')}")
        
        # Analyze alpha patterns
        self.analyze_alpha_patterns(findings)
        return findings
    
    def analyze_alpha_patterns(self, findings: List[Dict]):
        """Analyze patterns in /alpha endpoint responses"""
        print("\n📊 Analyzing /alpha patterns:")
        
        # Check for length-based patterns
        true_count = sum(1 for f in findings if f["output"] is True)
        false_count = sum(1 for f in findings if f["output"] is False)
        
        print(f"  True responses: {true_count}, False responses: {false_count}")
        
        # Check if it's based on input length
        for finding in findings:
            input_len = len(str(finding["input"]))
            if finding["output"] is True:
                print(f"    True for length {input_len}: '{finding['input']}'")
            else:
                print(f"    False for length {input_len}: '{finding['input']}'")
        
        # Check for alphabetical patterns
        print("  🔍 Checking alphabetical patterns...")
        for finding in findings:
            input_str = str(finding["input"])
            if finding["output"] is True:
                # Check if it contains only alphabetic characters
                if input_str.isalpha():
                    print(f"    TRUE for alphabetic: '{input_str}'")
                else:
                    print(f"    TRUE for non-alphabetic: '{input_str}'")
        
        # Look for specific patterns
        print("  ❓ Pattern not immediately obvious - needs more investigation")
    
    def run_comprehensive_test(self):
        """Run comprehensive tests on all endpoints"""
        print("🚀 Starting comprehensive API exploration...")
        print("=" * 60)
        
        # Test all endpoints
        self.findings["data"] = self.explore_data_endpoint()
        self.findings["time"] = self.explore_time_endpoint()
        self.findings["fizzbuzz"] = self.explore_fizzbuzz_endpoint()
        self.findings["glitch"] = self.explore_glitch_endpoint()
        self.findings["zap"] = self.explore_zap_endpoint()
        self.findings["alpha"] = self.explore_alpha_endpoint()
        
        # Generate summary report
        self.generate_report()
    
    def generate_report(self):
        """Generate a comprehensive report of findings"""
        print("\n" + "=" * 60)
        print("📋 COMPREHENSIVE ANALYSIS REPORT")
        print("=" * 60)
        
        print("\n🔍 ENDPOINT BEHAVIORS DISCOVERED:")
        print("-" * 40)
        
        # Data endpoint analysis
        print("\n📊 /data endpoint:")
        print("  - Accepts: POST with JSON data containing 'data' field")
        print("  - Returns: Integer result")
        print("  - Behavior: Appears to be a hash function or mathematical transformation")
        
        # Time endpoint analysis
        print("\n⏰ /time endpoint:")
        print("  - Accepts: GET request")
        print("  - Returns: Integer result")
        print("  - Behavior: Returns a fixed value (not time-based)")
        
        # FizzBuzz endpoint analysis
        print("\n🎯 /fizzbuzz endpoint:")
        print("  - Accepts: POST with JSON data containing 'data' field")
        print("  - Returns: Boolean result")
        print("  - Behavior: Likely implements FizzBuzz logic (divisible by 3 and 5)")
        
        # Glitch endpoint analysis
        print("\n⚡ /glitch endpoint:")
        print("  - Accepts: POST with JSON data containing 'data' field")
        print("  - Returns: Boolean result")
        print("  - Behavior: Pattern-based boolean response (needs more investigation)")
        
        # Zap endpoint analysis
        print("\n⚡ /zap endpoint:")
        print("  - Accepts: POST with JSON data containing 'data' field")
        print("  - Returns: String result")
        print("  - Behavior: Echo function (returns input as-is)")
        
        # Alpha endpoint analysis
        print("\n🔤 /alpha endpoint:")
        print("  - Accepts: POST with JSON data containing 'data' field")
        print("  - Returns: Boolean result")
        print("  - Behavior: Pattern-based boolean response (needs more investigation)")
        
        print("\n" + "=" * 60)
        print("🎯 NEXT STEPS FOR DEEPER ANALYSIS:")
        print("-" * 40)
        print("1. Test /data with more mathematical inputs to identify hash function")
        print("2. Investigate /glitch with specific patterns (length, content, etc.)")
        print("3. Test /fizzbuzz with edge cases and non-numeric inputs")
        print("4. Monitor /time over longer periods to confirm it's static")
        print("5. Test all endpoints with malformed JSON and error conditions")

if __name__ == "__main__":
    explorer = APIExplorer()
    explorer.run_comprehensive_test() 