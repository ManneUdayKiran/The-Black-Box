# Black Box API - Endpoint Analysis Logging Sheet

## 📋 Analysis Questions & Answers

For each endpoint, we answer these specific questions:
1. **Reverse the string?**
2. **Encode it (Base64)?**
3. **Filter characters?**
4. **Return the input length?**
5. **Do something based on input length?**

---

## 🔍 Endpoint Analysis Results

### 1. POST /data

| Question | Answer | Evidence |
|----------|--------|----------|
| **Reverse the string?** | ❌ **NO** | Input: "hello" → 1564557354 (not "olleh") |
| **Encode it (Base64)?** | ❌ **NO** | Output is integer, not Base64 string |
| **Filter characters?** | ❌ **NO** | All characters are processed equally |
| **Return the input length?** | ❌ **NO** | "hello" (5 chars) → 1564557354, not 5 |
| **Do something based on input length?** | ❌ **NO** | Length doesn't affect the hash algorithm |

**Actual Behavior**: MD5 hash function
- **Algorithm**: MD5(input) → first 8 hex chars → convert to integer
- **Examples**:
  - "hello" → 1564557354
  - "world" → 2105094199
  - "123" → 539801954
  - "" → 3558706393

---

### 2. GET /time

| Question | Answer | Evidence |
|----------|--------|----------|
| **Reverse the string?** | ❌ **NO** | No string input |
| **Encode it (Base64)?** | ❌ **NO** | Output is integer, not Base64 |
| **Filter characters?** | ❌ **NO** | No string processing |
| **Return the input length?** | ❌ **NO** | No input string |
| **Do something based on input length?** | ❌ **NO** | No input string |

**Actual Behavior**: Fixed value endpoint
- **Algorithm**: Returns hash value of "hello" (1564557354)
- **Examples**:
  - GET /time → 1564557354 (always the same)
  - Multiple calls return identical result

---

### 3. POST /fizzbuzz

| Question | Answer | Evidence |
|----------|--------|----------|
| **Reverse the string?** | ❌ **NO** | "15abc" → true (not reversed) |
| **Encode it (Base64)?** | ❌ **NO** | Output is boolean, not Base64 |
| **Filter characters?** | ✅ **YES** | Extracts only numeric characters using regex |
| **Return the input length?** | ❌ **NO** | "15abc" → true (not length 5) |
| **Do something based on input length?** | ❌ **NO** | Length doesn't affect the logic |

**Actual Behavior**: Number extraction + FizzBuzz logic
- **Algorithm**: Extract first number → check if divisible by both 3 and 5
- **Character Filtering**: Uses regex `\d+` to find numbers
- **Examples**:
  - "15" → true (divisible by 3 and 5)
  - "15abc" → true (extracts 15)
  - "abc15" → true (extracts 15)
  - "hello" → false (no numbers found)

---

### 4. POST /glitch

| Question | Answer | Evidence |
|----------|--------|----------|
| **Reverse the string?** | ❌ **NO** | "hello" → true (not reversed) |
| **Encode it (Base64)?** | ❌ **NO** | Output is boolean, not Base64 |
| **Filter characters?** | ✅ **YES** | Checks for specific keywords and character types |
| **Return the input length?** | ❌ **NO** | "hello" → true (not length 5) |
| **Do something based on input length?** | ✅ **YES** | Length affects the decision logic |

**Actual Behavior**: Multi-factor pattern recognition
- **Character Filtering**: 
  - Keywords: "glitch", "error", "bug", "fail"
  - Character types: letters, numbers, special characters
- **Length-Based Logic**:
  - Length divisible by 3 or 5 (if no numbers)
  - Special chars + length > 5
- **Examples**:
  - "glitch" → true (keyword)
  - "aaa" → true (length 3, no numbers)
  - "aaaaa" → true (length 5, no numbers)
  - "123" → false (numbers only)
  - "!@#$%" → true (special chars, length > 5)

---

### 5. POST /zap

| Question | Answer | Evidence |
|----------|--------|----------|
| **Reverse the string?** | ❌ **NO** | "hello" → "hello" (not "olleh") |
| **Encode it (Base64)?** | ❌ **NO** | "hello" → "hello" (not Base64 encoded) |
| **Filter characters?** | ❌ **NO** | All characters preserved exactly |
| **Return the input length?** | ❌ **NO** | "hello" → "hello" (not 5) |
| **Do something based on input length?** | ❌ **NO** | Length doesn't affect output |

**Actual Behavior**: Perfect echo function
- **Algorithm**: Return input string unchanged
- **Examples**:
  - "hello" → "hello"
  - "123" → "123"
  - "!@#$%" → "!@#$%"
  - "🚀" → "🚀"
  - "" → ""

---

### 6. POST /alpha

| Question | Answer | Evidence |
|----------|--------|----------|
| **Reverse the string?** | ❌ **NO** | "hello" → true (not reversed) |
| **Encode it (Base64)?** | ❌ **NO** | Output is boolean, not Base64 |
| **Filter characters?** | ✅ **YES** | Checks if ALL characters are alphabetic |
| **Return the input length?** | ❌ **NO** | "hello" → true (not length 5) |
| **Do something based on input length?** | ❌ **NO** | Length doesn't affect the logic |

**Actual Behavior**: Alphabetic character validation
- **Character Filtering**: Uses `isalpha()` to check if ALL characters are letters
- **Algorithm**: Return true if string contains only alphabetic characters
- **Examples**:
  - "hello" → true (all alphabetic)
  - "HELLO" → true (all alphabetic)
  - "123" → false (contains numbers)
  - "hello123" → false (mixed content)
  - "!@#" → false (contains symbols)
  - "" → false (empty string)

---

## 📊 Summary Table

| Endpoint | Reverse | Base64 | Filter | Length | Length-Based Logic |
|----------|---------|--------|--------|--------|-------------------|
| **/data** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **/time** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **/fizzbuzz** | ❌ | ❌ | ✅ | ❌ | ❌ |
| **/glitch** | ❌ | ❌ | ✅ | ❌ | ✅ |
| **/zap** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **/alpha** | ❌ | ❌ | ✅ | ❌ | ❌ |

---

## 🔍 Detailed Character Filtering Analysis

### /fizzbuzz - Number Extraction
- **Filter Type**: Regex-based number extraction
- **Pattern**: `\d+` (one or more digits)
- **Behavior**: Finds first sequence of digits in string
- **Examples**:
  - "15abc" → extracts "15"
  - "abc15" → extracts "15"
  - "hello" → no numbers found

### /glitch - Multi-Factor Filtering
- **Keyword Filtering**: Checks for specific words
- **Character Type Filtering**: Distinguishes letters, numbers, symbols
- **Length-Based Filtering**: Considers string length in decision logic
- **Examples**:
  - "glitch" → keyword match
  - "123" → numbers only (rejected)
  - "!@#$%" → special characters + length > 5

### /alpha - Alphabetic Validation
- **Filter Type**: Complete string validation
- **Method**: `isalpha()` - checks if ALL characters are letters
- **Behavior**: Rejects any non-alphabetic characters
- **Examples**:
  - "hello" → all alphabetic (accepted)
  - "hello123" → mixed content (rejected)
  - "!@#" → symbols (rejected)

---

## 📝 Key Findings

1. **No String Reversal**: None of the endpoints reverse the input string
2. **No Base64 Encoding**: None of the endpoints use Base64 encoding
3. **Character Filtering**: 3 endpoints use character filtering:
   - `/fizzbuzz`: Extracts numbers using regex
   - `/glitch`: Multi-factor character analysis
   - `/alpha`: Validates alphabetic-only content
4. **No Length Return**: None return the input string length
5. **Length-Based Logic**: Only `/glitch` uses input length in its decision logic

---

## 🎯 Conclusion

The Black Box API endpoints primarily focus on:
- **Hash functions** (/data)
- **Fixed values** (/time)
- **Pattern recognition** (/fizzbuzz, /glitch, /alpha)
- **Echo functionality** (/zap)

None of the endpoints perform string reversal, Base64 encoding, or return input length. Character filtering and length-based logic are used selectively in specific endpoints for pattern recognition and validation. 