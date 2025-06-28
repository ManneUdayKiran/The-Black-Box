# Black Box API Explorer

This project contains tools to reverse-engineer mysterious API endpoints at `https://blackbox-interface.vercel.app/`. The goal is to understand what each endpoint does through systematic testing and pattern analysis.

## 🎯 Challenge Overview

You are dropped into a malfunctioning system filled with mysterious API endpoints. With no documentation or hints, each endpoint behaves in unpredictable ways. Your goal is to reverse-engineer what each API does by crafting inputs, analyzing outputs, and documenting your discoveries.

## 🔍 Available Endpoints

1. **POST /data** - Accepts string data, returns integer
2. **GET /time** - No input, returns integer
3. **POST /fizzbuzz** - Accepts string data, returns boolean
4. **POST /glitch** - Accepts string data, returns boolean
5. **POST /zap** - Accepts string data, returns string

## 🛠️ Tools Included

### 1. Basic API Explorer (`api_explorer.py`)
- Systematic testing of all endpoints
- Pattern recognition and analysis
- Comprehensive reporting

### 2. Advanced API Tester (`advanced_tester.py`)
- Deep pattern analysis
- Mathematical function detection
- Advanced test cases

## 🚀 Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Running the Basic Explorer
```bash
python api_explorer.py
```

### Running the Advanced Tester
```bash
python advanced_tester.py
```

## 📊 Current Findings

### /data Endpoint
- **Method**: POST
- **Input**: JSON with "data" field (string)
- **Output**: Integer
- **Behavior**: Appears to be a hash function or mathematical transformation of the input string

### /time Endpoint
- **Method**: GET
- **Input**: None
- **Output**: Integer
- **Behavior**: Returns a fixed value (not time-based)

### /fizzbuzz Endpoint
- **Method**: POST
- **Input**: JSON with "data" field (string)
- **Output**: Boolean
- **Behavior**: Implements classic FizzBuzz logic - returns true for numbers divisible by both 3 and 5

### /glitch Endpoint
- **Method**: POST
- **Input**: JSON with "data" field (string)
- **Output**: Boolean
- **Behavior**: Pattern-based boolean response (length/content analysis needed)

### /zap Endpoint
- **Method**: POST
- **Input**: JSON with "data" field (string)
- **Output**: String
- **Behavior**: Echo function - returns input as-is

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

## 🎯 Next Steps

1. **Deep Pattern Analysis**: Continue investigating the exact algorithms used
2. **Error Handling**: Test with malformed JSON and edge cases
3. **Performance Testing**: Test with very large inputs
4. **Documentation**: Create detailed documentation of each endpoint's behavior

## 🤝 Contributing

Feel free to add more test cases, improve pattern recognition algorithms, or enhance the analysis tools!

## 📄 License

This project is for educational purposes and API exploration. 