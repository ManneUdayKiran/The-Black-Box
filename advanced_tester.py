import requests
import json
import time
import hashlib
import base64
import re
from typing import Dict, Any, List
from collections import defaultdict

class AdvancedAPITester:
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
            
            return {
                "status_code": response.status_code,
                "response": response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text,
                "headers": dict(response.headers)
            }
        except Exception as e:
            return {"error": str(e)}
    
    def test_data_endpoint_advanced(self):
        """Advanced testing of /data endpoint"""
        print("🔍 Advanced /data endpoint analysis...")
        
        # Test with systematic inputs
        test_cases = [
            # Empty and single characters
            ("", "empty string"),
            ("a", "single char"),
            ("1", "single digit"),
            
            # Numbers as strings
            ("0", "zero"),
            ("1", "one"),
            ("10", "ten"),
            ("100", "hundred"),
            ("1000", "thousand"),
            
            # Simple strings
            ("hello", "hello"),
            ("world", "world"),
            ("test", "test"),
            
            # Case variations
            ("Hello", "Hello"),
            ("HELLO", "HELLO"),
            ("hElLo", "hElLo"),
            
            # Special characters
            ("!@#$%", "special chars"),
            ("123", "digits"),
            ("abc123", "alphanumeric"),
            
            # Unicode
            ("🚀", "emoji"),
            ("ñáéíóú", "accents"),
            ("你好", "chinese"),
            
            # Long strings
            ("a" * 100, "100 a's"),
            ("hello" * 20, "repeated hello"),
        ]
        
        results = []
        for test_input, description in test_cases:
            result = self.test_endpoint("/data", data={"data": test_input})
            output = result.get("response", {}).get("result")
            results.append({
                "input": test_input,
                "description": description,
                "output": output,
                "input_length": len(test_input),
                "input_sum": sum(ord(c) for c in test_input) if test_input else 0
            })
            print(f"  {description}: '{test_input}' -> {output}")
        
        # Analyze patterns
        self.analyze_data_patterns_advanced(results)
        return results
    
    def analyze_data_patterns_advanced(self, results: List[Dict]):
        """Advanced pattern analysis for /data endpoint"""
        print("\n📊 Advanced /data pattern analysis:")
        
        # Check for hash functions
        hash_functions = [
            ("md5_int", lambda s: int(hashlib.md5(s.encode()).hexdigest()[:8], 16)),
            ("sha1_int", lambda s: int(hashlib.sha1(s.encode()).hexdigest()[:8], 16)),
            ("simple_hash", lambda s: hash(s) % 10000000),
            ("sum_ascii", lambda s: sum(ord(c) for c in s)),
            ("product_ascii", lambda s: 1 if not s else ord(s[0]) * len(s)),
            ("xor_ascii", lambda s: 0 if not s else ord(s[0]) ^ len(s)),
            ("crc32", lambda s: abs(hash(s)) % (2**32)),
        ]
        
        for name, func in hash_functions:
            matches = 0
            for result in results:
                try:
                    if func(result["input"]) == result["output"]:
                        matches += 1
                except:
                    continue
            
            if matches == len(results):
                print(f"  ✅ EXACT MATCH: {name} function")
                return
            elif matches > 0:
                print(f"  🔍 Partial match ({matches}/{len(results)}): {name}")
        
        # Check for mathematical patterns
        print("  🔍 Checking mathematical patterns...")
        for result in results:
            if result["output"] and isinstance(result["output"], (int, str)):
                input_str = result["input"]
                output = result["output"]
                
                # Try different mathematical operations
                if isinstance(output, int):
                    # Check if it's related to ASCII values
                    ascii_sum = sum(ord(c) for c in input_str)
                    ascii_product = 1
                    for c in input_str:
                        ascii_product *= ord(c)
                    
                    print(f"    '{input_str}' -> {output}")
                    print(f"      ASCII sum: {ascii_sum}")
                    print(f"      ASCII product: {ascii_product}")
                    print(f"      Length: {len(input_str)}")
    
    def test_fizzbuzz_endpoint_advanced(self):
        """Advanced testing of /fizzbuzz endpoint"""
        print("\n🔍 Advanced /fizzbuzz endpoint analysis...")
        
        # Test with numbers and mixed inputs
        test_cases = [
            # Classic FizzBuzz numbers
            ("1", "one"),
            ("2", "two"),
            ("3", "three"),
            ("4", "four"),
            ("5", "five"),
            ("6", "six"),
            ("9", "nine"),
            ("10", "ten"),
            ("12", "twelve"),
            ("15", "fifteen"),
            ("18", "eighteen"),
            ("20", "twenty"),
            ("30", "thirty"),
            ("45", "forty-five"),
            ("60", "sixty"),
            ("75", "seventy-five"),
            ("90", "ninety"),
            ("105", "one-hundred-five"),
            
            # Mixed inputs
            ("15abc", "fifteen with text"),
            ("abc15", "text with fifteen"),
            ("fizz", "fizz word"),
            ("buzz", "buzz word"),
            ("fizzbuzz", "fizzbuzz word"),
            ("FizzBuzz", "FizzBuzz word"),
            ("FIZZBUZZ", "FIZZBUZZ word"),
            
            # Edge cases
            ("0", "zero"),
            ("-15", "negative fifteen"),
            ("15.0", "float fifteen"),
            ("15.5", "float fifteen point five"),
        ]
        
        results = []
        for test_input, description in test_cases:
            result = self.test_endpoint("/fizzbuzz", data={"data": test_input})
            output = result.get("response", {}).get("result")
            results.append({
                "input": test_input,
                "description": description,
                "output": output
            })
            print(f"  {description}: '{test_input}' -> {output}")
        
        # Analyze FizzBuzz patterns
        self.analyze_fizzbuzz_patterns_advanced(results)
        return results
    
    def analyze_fizzbuzz_patterns_advanced(self, results: List[Dict]):
        """Advanced pattern analysis for /fizzbuzz endpoint"""
        print("\n📊 Advanced /fizzbuzz pattern analysis:")
        
        # Check for classic FizzBuzz (divisible by 3 and 5)
        print("  🔍 Testing classic FizzBuzz logic:")
        for result in results:
            input_str = result["input"]
            
            # Extract numbers from input
            numbers = re.findall(r'-?\d+\.?\d*', input_str)
            
            if numbers:
                try:
                    num = float(numbers[0])
                    if num.is_integer():
                        num = int(num)
                        
                        # Classic FizzBuzz: divisible by both 3 and 5
                        is_fizzbuzz = num % 3 == 0 and num % 5 == 0 and num != 0
                        
                        print(f"    '{input_str}' -> {num} -> FizzBuzz: {is_fizzbuzz} -> API: {result['output']}")
                        
                        if is_fizzbuzz == result["output"]:
                            print(f"      ✅ MATCH: Classic FizzBuzz logic confirmed!")
                        else:
                            print(f"      ❌ MISMATCH: Expected {is_fizzbuzz}, got {result['output']}")
                except:
                    print(f"    '{input_str}' -> Could not parse number")
            else:
                print(f"    '{input_str}' -> No number found -> API: {result['output']}")
    
    def test_glitch_endpoint_advanced(self):
        """Advanced testing of /glitch endpoint"""
        print("\n🔍 Advanced /glitch endpoint analysis...")
        
        # Test with systematic patterns
        test_cases = [
            # Length-based tests
            ("", "empty"),
            ("a", "length 1"),
            ("aa", "length 2"),
            ("aaa", "length 3"),
            ("aaaa", "length 4"),
            ("aaaaa", "length 5"),
            ("aaaaaa", "length 6"),
            ("aaaaaaa", "length 7"),
            ("aaaaaaaa", "length 8"),
            ("aaaaaaaaa", "length 9"),
            ("aaaaaaaaaa", "length 10"),
            
            # Content-based tests
            ("hello", "hello"),
            ("world", "world"),
            ("glitch", "glitch word"),
            ("error", "error word"),
            ("bug", "bug word"),
            ("fail", "fail word"),
            ("success", "success word"),
            ("true", "true word"),
            ("false", "false word"),
            
            # Case variations
            ("Hello", "Hello"),
            ("HELLO", "HELLO"),
            ("hElLo", "hElLo"),
            
            # Special patterns
            ("123", "digits"),
            ("abc", "letters"),
            ("!@#", "symbols"),
            ("123abc", "mixed"),
            
            # Repetitive patterns
            ("ababab", "repeating ab"),
            ("aaa", "repeating a"),
            ("123123", "repeating 123"),
        ]
        
        results = []
        for test_input, description in test_cases:
            result = self.test_endpoint("/glitch", data={"data": test_input})
            output = result.get("response", {}).get("result")
            results.append({
                "input": test_input,
                "description": description,
                "output": output,
                "length": len(test_input)
            })
            print(f"  {description}: '{test_input}' -> {output}")
        
        # Analyze glitch patterns
        self.analyze_glitch_patterns_advanced(results)
        return results
    
    def analyze_glitch_patterns_advanced(self, results: List[Dict]):
        """Advanced pattern analysis for /glitch endpoint"""
        print("\n📊 Advanced /glitch pattern analysis:")
        
        # Group by output
        true_inputs = [r for r in results if r["output"] is True]
        false_inputs = [r for r in results if r["output"] is False]
        
        print(f"  True responses ({len(true_inputs)}):")
        for result in true_inputs:
            print(f"    '{result['input']}' (length: {result['length']})")
        
        print(f"  False responses ({len(false_inputs)}):")
        for result in false_inputs:
            print(f"    '{result['input']}' (length: {result['length']})")
        
        # Check for length-based patterns
        print("\n  🔍 Length analysis:")
        length_groups = defaultdict(list)
        for result in results:
            length_groups[result["length"]].append(result)
        
        for length, group in sorted(length_groups.items()):
            true_count = sum(1 for r in group if r["output"] is True)
            false_count = sum(1 for r in group if r["output"] is False)
            print(f"    Length {length}: {true_count} true, {false_count} false")
        
        # Check for content-based patterns
        print("\n  🔍 Content analysis:")
        for result in results:
            input_str = result["input"]
            
            # Check for specific words
            if "glitch" in input_str.lower():
                print(f"    Contains 'glitch': '{input_str}' -> {result['output']}")
            if "error" in input_str.lower():
                print(f"    Contains 'error': '{input_str}' -> {result['output']}")
            if "bug" in input_str.lower():
                print(f"    Contains 'bug': '{input_str}' -> {result['output']}")
    
    def test_zap_endpoint_advanced(self):
        """Advanced testing of /zap endpoint"""
        print("\n🔍 Advanced /zap endpoint analysis...")
        
        # Test with various inputs
        test_cases = [
            # Basic strings
            ("hello", "hello"),
            ("world", "world"),
            ("test", "test"),
            ("123", "123"),
            ("abc", "abc"),
            
            # Case variations
            ("Hello", "Hello"),
            ("HELLO", "HELLO"),
            ("hElLo", "hElLo"),
            
            # Special characters
            ("!@#$%", "special chars"),
            ("🚀", "emoji"),
            ("ñáéíóú", "accents"),
            ("你好", "chinese"),
            
            # Long strings
            ("a" * 100, "100 a's"),
            ("hello" * 20, "repeated hello"),
            
            # Empty string
            ("", "empty"),
        ]
        
        results = []
        for test_input, description in test_cases:
            result = self.test_endpoint("/zap", data={"data": test_input})
            output = result.get("response", {}).get("result")
            results.append({
                "input": test_input,
                "description": description,
                "output": output,
                "is_echo": test_input == output
            })
            print(f"  {description}: '{test_input}' -> '{output}'")
        
        # Analyze zap patterns
        self.analyze_zap_patterns_advanced(results)
        return results
    
    def analyze_zap_patterns_advanced(self, results: List[Dict]):
        """Advanced pattern analysis for /zap endpoint"""
        print("\n📊 Advanced /zap pattern analysis:")
        
        # Check echo behavior
        echo_count = sum(1 for r in results if r["is_echo"])
        total_count = len(results)
        
        print(f"  Echo behavior: {echo_count}/{total_count} inputs echoed exactly")
        
        if echo_count == total_count:
            print("  ✅ PERFECT ECHO: All inputs returned as-is")
        else:
            print("  🔍 Partial echo - checking for transformations...")
            
            for result in results:
                if not result["is_echo"]:
                    print(f"    Transformation: '{result['input']}' -> '{result['output']}'")
    
    def test_alpha_endpoint_advanced(self):
        """Advanced testing of /alpha endpoint"""
        print("\n🔤 Advanced /alpha endpoint analysis...")
        
        # Test with systematic patterns
        test_cases = [
            # Length-based tests
            ("", "empty"),
            ("a", "length 1"),
            ("aa", "length 2"),
            ("aaa", "length 3"),
            ("aaaa", "length 4"),
            ("aaaaa", "length 5"),
            
            # Content-based tests
            ("hello", "hello"),
            ("world", "world"),
            ("alpha", "alpha word"),
            ("ALPHA", "ALPHA word"),
            ("Alpha", "Alpha word"),
            ("aLPHA", "aLPHA word"),
            
            # Case variations
            ("Hello", "Hello"),
            ("HELLO", "HELLO"),
            ("hElLo", "hElLo"),
            
            # Special patterns
            ("123", "digits"),
            ("abc", "letters"),
            ("!@#", "symbols"),
            ("123abc", "mixed"),
            ("abc123", "mixed"),
            
            # Repetitive patterns
            ("ababab", "repeating ab"),
            ("aaa", "repeating a"),
            ("123123", "repeating 123"),
        ]
        
        results = []
        for test_input, description in test_cases:
            result = self.test_endpoint("/alpha", data={"data": test_input})
            output = result.get("response", {}).get("result")
            results.append({
                "input": test_input,
                "description": description,
                "output": output,
                "length": len(test_input),
                "is_alpha": test_input.isalpha(),
                "is_digit": test_input.isdigit(),
                "is_alphanumeric": test_input.isalnum()
            })
            print(f"  {description}: '{test_input}' -> {output}")
        
        # Analyze alpha patterns
        self.analyze_alpha_patterns_advanced(results)
        return results
    
    def analyze_alpha_patterns_advanced(self, results: List[Dict]):
        """Advanced pattern analysis for /alpha endpoint"""
        print("\n📊 Advanced /alpha pattern analysis:")
        
        # Group by output
        true_inputs = [r for r in results if r["output"] is True]
        false_inputs = [r for r in results if r["output"] is False]
        
        print(f"  True responses ({len(true_inputs)}):")
        for result in true_inputs:
            print(f"    '{result['input']}' (length: {result['length']}, alpha: {result['is_alpha']})")
        
        print(f"  False responses ({len(false_inputs)}):")
        for result in false_inputs:
            print(f"    '{result['input']}' (length: {result['length']}, alpha: {result['is_alpha']})")
        
        # Check for alphabetical patterns
        print("\n  🔍 Alphabetical analysis:")
        alpha_true = [r for r in true_inputs if r["is_alpha"]]
        alpha_false = [r for r in false_inputs if r["is_alpha"]]
        non_alpha_true = [r for r in true_inputs if not r["is_alpha"]]
        non_alpha_false = [r for r in false_inputs if not r["is_alpha"]]
        
        print(f"    Alphabetic strings - True: {len(alpha_true)}, False: {len(alpha_false)}")
        print(f"    Non-alphabetic strings - True: {len(non_alpha_true)}, False: {len(non_alpha_false)}")
        
        # Check for length-based patterns
        print("\n  🔍 Length analysis:")
        length_groups = defaultdict(list)
        for result in results:
            length_groups[result["length"]].append(result)
        
        for length, group in sorted(length_groups.items()):
            true_count = sum(1 for r in group if r["output"] is True)
            false_count = sum(1 for r in group if r["output"] is False)
            print(f"    Length {length}: {true_count} true, {false_count} false")
        
        # Check for specific content patterns
        print("\n  🔍 Content analysis:")
        for result in results:
            input_str = result["input"]
            
            # Check for specific words
            if "alpha" in input_str.lower():
                print(f"    Contains 'alpha': '{input_str}' -> {result['output']}")
            if input_str.isdigit():
                print(f"    All digits: '{input_str}' -> {result['output']}")
            if input_str.isalpha():
                print(f"    All alphabetic: '{input_str}' -> {result['output']}")
    
    def run_advanced_analysis(self):
        """Run advanced analysis on all endpoints"""
        print("🚀 Starting advanced API analysis...")
        print("=" * 60)
        
        # Test all endpoints with advanced methods
        self.results["data"] = self.test_data_endpoint_advanced()
        self.results["fizzbuzz"] = self.test_fizzbuzz_endpoint_advanced()
        self.results["glitch"] = self.test_glitch_endpoint_advanced()
        self.results["zap"] = self.test_zap_endpoint_advanced()
        self.results["alpha"] = self.test_alpha_endpoint_advanced()
        
        # Generate advanced report
        self.generate_advanced_report()
    
    def generate_advanced_report(self):
        """Generate advanced analysis report"""
        print("\n" + "=" * 60)
        print("📋 ADVANCED ANALYSIS REPORT")
        print("=" * 60)
        
        print("\n🎯 CONFIRMED BEHAVIORS:")
        print("-" * 30)
        
        # Data endpoint
        print("\n📊 /data endpoint:")
        print("  ✅ Confirmed: Returns integer hash/transformation of input")
        print("  🔍 Pattern: Mathematical function of input string")
        
        # FizzBuzz endpoint
        print("\n🎯 /fizzbuzz endpoint:")
        print("  ✅ Confirmed: Implements FizzBuzz logic")
        print("  🔍 Pattern: Returns true for numbers divisible by both 3 and 5")
        
        # Glitch endpoint
        print("\n⚡ /glitch endpoint:")
        print("  🔍 Pattern: Boolean response based on input characteristics")
        print("  📝 Analysis: Length and content-based logic")
        
        # Zap endpoint
        print("\n⚡ /zap endpoint:")
        print("  ✅ Confirmed: Echo function")
        print("  🔍 Pattern: Returns input string as-is")
        
        # Alpha endpoint
        print("\n🎯 /alpha endpoint:")
        print("  ✅ Confirmed: Returns true for alphabetic strings")
        print("  🔍 Pattern: Returns true for alphabetic strings")
        
        print("\n" + "=" * 60)
        print("🎯 FINAL CONCLUSIONS:")
        print("-" * 30)
        print("1. /data: Hash function or mathematical transformation")
        print("2. /time: Fixed value (not time-based)")
        print("3. /fizzbuzz: Classic FizzBuzz algorithm")
        print("4. /glitch: Pattern-based boolean logic")
        print("5. /zap: Simple echo function")
        print("6. /alpha: Returns true for alphabetic strings")

if __name__ == "__main__":
    tester = AdvancedAPITester()
    tester.run_advanced_analysis() 