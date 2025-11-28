# Prime Number C Extension - Workflow & Architecture

## 📋 Project Overview
```
Prime Number C Extension Project
├── C Extension (High Performance)
├── Python Wrapper (Easy Interface) 
├── Benchmark Testing (Performance Comparison)
└── Documentation (Usage & Setup)
```

## 🔄 Build & Execution Flow

```
1. SOURCE CODE
   ┌─────────────────┐    ┌─────────────────┐
   │    setup.py     │    │ prime_module.c  │
   │  (Build Config) │    │  (C Extension)  │
   └─────────────────┘    └─────────────────┘
           │                       │
           └───────────┬───────────┘
                       │
2. COMPILATION         ▼
   ┌─────────────────────────────────────┐
   │  python setup.py build_ext --inplace │
   │            (GCC Compiler)            │
   └─────────────────────────────────────┘
                       │
3. OUTPUT              ▼
   ┌─────────────────────────────────────┐
   │     prime.cpython-312-*.so          │
   │        (Compiled Library)           │
   └─────────────────────────────────────┘
                       │
4. TESTING             ▼
   ┌─────────────────────────────────────┐
   │            test.py                  │
   │    (Benchmark & Comparison)         │
   └─────────────────────────────────────┘
```

## ⚙️ Module Interactions

### Core Functions:
- **C Extension**: `isPrime(n)` → `sum_primes(N)`
- **Python Version**: `is_prime(n)` → `sum_primesPY(N)`

### Data Flow:
```
Input (N) → isPrime() → sum_primes() → Result
    ↓
test.py benchmarks both implementations
    ↓
Performance comparison output
```

## 📊 Performance Results
- **C Extension**: ~2-5 seconds for N=10M
- **Pure Python**: ~60-150 seconds for N=10M  
- **Speed Improvement**: 10-50x faster with C

## 🛠️ Quick Commands
```bash
# Build extension
python3 setup.py build_ext --inplace

# Run benchmark
python3 test.py

# Test specific function
python3 -c "import prime; print(prime.sum_primes(1000))"
```

## 📁 File Structure
```
prime_ext/
├── prime_module.c      # C implementation
├── setup.py           # Build configuration  
├── test.py           # Performance testing
├── prime.so          # Compiled extension (generated)
├── README.md         # Documentation
└── .gitignore        # Git exclusions
```

## 🔧 Key Components

**1. C Extension (prime_module.c)**
- Fast prime checking algorithm
- Python C API integration
- Memory efficient implementation

**2. Python Interface (test.py)**
- Import compiled extension
- Benchmark comparison
- Memory & time profiling

**3. Build System (setup.py)**
- setuptools configuration
- Compiler integration
- Cross-platform support