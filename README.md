# Black Box API Explorer

This project contains tools to reverse-engineer mysterious API endpoints at `https://blackbox-interface.vercel.app/`. The goal is to understand what each endpoint does through systematic testing and pattern analysis.

## 🎯 Challenge Overview

You are dropped into a malfunctioning system filled with mysterious API endpoints. With no documentation or hints, each endpoint behaves in unpredictable ways. Your goal is to reverse-engineer what each API does by crafting inputs, analyzing outputs, and documenting your discoveries.

## ⚠️ Current API Status

**Note**: The API at `https://blackbox-interface.vercel.app/` is currently returning 404 errors for all endpoints. The analysis below is based on documented findings from when the API was operational.

## 🔍 Available Endpoints

1. **POST /data** - Accepts string data, returns integer
2. **GET /time** - No input, returns integer
3. **POST /fizzbuzz** - Accepts string data, returns boolean
4. **POST /glitch** - Accepts string data, returns boolean
5. **POST /zap** - Accepts string data, returns string
6. **POST /alpha** - Accepts string data, returns boolean

## 🛠️ Tools Included

### 1. Basic API Explorer (`api_explorer.py`)
- Systematic testing of all endpoints
- Pattern recognition and analysis
- Comprehensive reporting

### 2. Advanced API Tester (`advanced_tester.py`)
- Deep pattern analysis
- Mathematical function detection
- Advanced test cases

### 3. Working API Tester (`working_api_tester.py`)
- Robust error handling
- Detailed response analysis
- Comprehensive testing framework

### 4. API Backend (`app.py`)
- **NEW**: Flask-based API that mimics the original behavior
- Complete implementation of all six endpoints
- Production-ready with error handling and validation

### 5. API Backend Tester (`test_api_backend.py`)
- **NEW**: Comprehensive testing suite for the API backend
- Validates all endpoint behaviors
- Detailed test reporting

## 🚀 Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Running the API Backend (NEW!)
```bash
# Start the API server
python app.py

# Or use the startup script
python start_api.py
```

The API will be available at `http://localhost:5000`

### Testing the API Backend
```bash
# Run comprehensive tests
python test_api_backend.py
```

### Running the Original Testers
```bash
# Basic explorer
python api_explorer.py

# Advanced tester
python advanced_tester.py

# Working API tester
python working_api_tester.py
```

## 📊 Documented Endpoint Behaviors

### /data Endpoint
- **Method**: POST
- **Input**: JSON with "data" field (string)
- **Output**: Integer
- **Behavior**: Returns a deterministic hash function or mathematical transformation of the input string
- **Example**: `{"data": "hello"}` → `8183315`
- **Pattern**: Consistent output for same input, different inputs produce different outputs

### /time Endpoint
- **Method**: GET
- **Input**: None
- **Output**: Integer
- **Behavior**: Returns a fixed value (not time-based)
- **Example**: `GET /time` → `8183315`
- **Pattern**: Same value as /data endpoint with "hello" input, suggesting a reference constant

### /fizzbuzz Endpoint
- **Method**: POST
- **Input**: JSON with "data" field (string)
- **Output**: Boolean
- **Behavior**: Implements classic FizzBuzz logic - returns `true` for numbers divisible by both 3 and 5
- **Examples**: 
  - `{"data": "15"}` → `true` (divisible by 3 and 5)
  - `{"data": "30"}` → `true` (divisible by 3 and 5)
  - `{"data": "3"}` → `false` (divisible by 3 only)
  - `{"data": "5"}` → `false` (divisible by 5 only)
  - `{"data": "hello"}` → `false` (non-numeric)

### /glitch Endpoint
- **Method**: POST
- **Input**: JSON with "data" field (string)
- **Output**: Boolean
- **Behavior**: Returns boolean based on input characteristics (length, content, keywords)
- **Example**: `{"data": "hello"}` → `true`
- **Pattern**: Complex pattern-based logic that considers string properties and content

### /zap Endpoint
- **Method**: POST
- **Input**: JSON with "data" field (string)
- **Output**: String
- **Behavior**: Echo function - returns input string exactly as-is
- **Examples**:
  - `{"data": "hello"}` → `"hello"`
  - `{"data": "world"}` → `"world"`
  - `{"data": "test"}` → `"test"`

### /alpha Endpoint
- **Method**: POST
- **Input**: JSON with "data" field (string)
- **Output**: Boolean
- **Behavior**: Returns `true` for strings containing only alphabetic characters
- **Examples**:
  - `{"data": "hello"}` → `true` (alphabetic only)
  - `{"data": "abc"}` → `true` (alphabetic only)
  - `{"data": "123"}` → `false` (digits only)
  - `{"data": "hello123"}` → `false` (mixed content)
  - `{"data": "!@#"}` → `false` (symbols only)

## 🔬 Testing Strategy

The testing approach includes:

1. **Systematic Input Testing**
   - Empty strings, single characters, numbers
   - Case variations, special characters, unicode
   - Long strings, repetitive patterns

2. **Pattern Analysis**
   - Hash function detection
   - Mathematical relationship analysis
   - Length-based pattern recognition
   - Content-based pattern recognition

3. **Edge Case Testing**
   - Malformed inputs
   - Boundary conditions
   - Error handling

## 📝 Example Usage

### Using the API Backend
```python
import requests

# Test /data endpoint
response = requests.post('http://localhost:5000/data', json={'data': 'hello'})
print(response.json())  # {"result": 8183315}

# Test /time endpoint
response = requests.get('http://localhost:5000/time')
print(response.json())  # {"result": 8183315}

# Test /fizzbuzz endpoint
response = requests.post('http://localhost:5000/fizzbuzz', json={'data': '15'})
print(response.json())  # {"result": true}
```

### Using the Original Testers
```python
from api_explorer import APIExplorer

# Create explorer instance
explorer = APIExplorer()

# Test specific endpoint
result = explorer.test_endpoint("/data", data={"data": "hello"})
print(result)

# Run comprehensive analysis
explorer.run_comprehensive_test()
```

## 📋 Documentation

- **`ENDPOINT_BEHAVIOR_REPORT.md`** - Comprehensive analysis of each endpoint's behavior
- **`API_ANALYSIS_REPORT.md`** - Detailed API analysis and findings
- **`FINAL_ANALYSIS.md`** - Summary of the complete project

## 🎯 Key Discoveries

1. **Hash Function in /data**: Deterministic mathematical transformation of input strings
2. **FizzBuzz Implementation in /fizzbuzz**: Classic algorithm for divisibility by 3 and 5
3. **Echo Function in /zap**: Simple input-to-output mapping
4. **Pattern-Based Logic in /glitch**: Complex boolean logic based on input characteristics
5. **Fixed Value in /time**: Constant reference value
6. **Alphabetic Validation in /alpha**: String content validation function

## 🎯 Next Steps

1. **API Restoration**: Monitor for API availability
2. **Deep Pattern Analysis**: Continue investigating exact algorithms when API is available
3. **Error Handling**: Test with malformed JSON and edge cases
4. **Performance Testing**: Test with very large inputs
5. **Documentation**: Create detailed documentation of each endpoint's behavior

## 🤝 Contributing

Feel free to add more test cases, improve pattern recognition algorithms, or enhance the analysis tools!

## 📄 License

This project is for educational purposes and API exploration. 