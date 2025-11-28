# Prime Number C Extension

A high-performance Python C extension for prime number calculations. This project demonstrates the significant performance improvements achievable by implementing computationally intensive algorithms in C rather than pure Python.

## Overview

This extension provides optimized prime number functions written in C and exposed to Python through the Python C API. The main function calculates the sum of all prime numbers up to a given limit N.

## Features

- **High Performance**: C implementation provides significant speed improvements over pure Python
- **Memory Efficient**: Optimized memory usage for large computations
- **Easy Integration**: Simple Python interface for C functions
- **Benchmarking**: Includes comprehensive performance comparison tools

## Project Structure

```
prime_ext/
├── prime_module.c    # C extension source code
├── setup.py          # Build configuration
├── test.py          # Benchmarking and testing script
├── build/           # Build artifacts (auto-generated)
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## Installation

### Prerequisites
- Python 3.6 or higher
- GCC or compatible C compiler
- Python development headers (`python3-dev` on Ubuntu/Debian)

### Build the Extension

1. Clone or download the project
2. Navigate to the project directory:
   ```bash
   cd prime_ext
   ```

3. Build the extension:
   ```bash
   python setup.py build_ext --inplace
   ```

   Or install it:
   ```bash
   python setup.py install
   ```

## Usage

### Basic Usage

```python
import prime

# Calculate sum of primes up to 1,000,000
result = prime.sum_primes(1000000)
print(f"Sum of primes up to 1,000,000: {result}")
```

### Performance Comparison

Run the included benchmark script:

```bash
python test.py
```

This will compare the performance of:
- C extension implementation (`prime.sum_primes`)
- Pure Python implementation (`sum_primesPY`)

## Performance Results

The C extension typically shows dramatic performance improvements:

- **Speed**: 10-50x faster than pure Python implementation
- **Memory**: More efficient memory usage
- **Scalability**: Better performance scaling for larger inputs

Example benchmark results for N=10,000,000:
- C Extension: ~2-5 seconds
- Pure Python: ~60-150 seconds

## Algorithm

Both implementations use the same optimized prime-checking algorithm:

1. Handle special cases (n ≤ 1, n = 2, n = 3)
2. Check divisibility by 2 and 3
3. Check potential divisors of the form 6k±1 up to √n
4. Sum all identified prime numbers

## Development

### Modifying the C Code

1. Edit `prime_module.c`
2. Rebuild the extension:
   ```bash
   python setup.py build_ext --inplace
   ```
3. Test your changes:
   ```bash
   python test.py
   ```

### Adding New Functions

To add new functions to the C extension:

1. Implement the function in C in `prime_module.c`
2. Add the method definition to `PrimeMethods` array
3. Rebuild the extension

## Troubleshooting

### Build Issues
- Ensure you have Python development headers installed
- Check that your compiler supports C99 or later
- Verify Python and pip are up to date

### Import Issues
- Make sure the extension was built successfully
- Check that the `.so` file was created in the project directory
- Verify you're running Python from the correct directory

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is provided as-is for educational and demonstration purposes.

## Technical Details

- **Language**: C (extension) + Python (interface & testing)
- **Build System**: setuptools
- **Target**: CPython 3.6+
- **Compiler**: GCC/Clang compatible
- **Dependencies**: Python C API

---

*This project demonstrates the power of C extensions for performance-critical Python applications.*