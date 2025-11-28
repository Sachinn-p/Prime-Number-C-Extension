#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdbool.h>

static bool isPrime(int n) {
  
    if (n <= 1)
        return false;

    if (n == 2 || n == 3)
        return true;

    if (n % 2 == 0 || n % 3 == 0)
        return false;
    
    for (int i = 5; i*i<=n; i = i + 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;

    return true;
}

static PyObject* sum_primes(PyObject* self, PyObject* args) {
    int N;
    if (!PyArg_ParseTuple(args, "i", &N))
        return NULL;

    long sum = 0;

    for (int i = 2; i <= N; i++) {
        if (isPrime(i))
            sum += i;
    }

    return PyLong_FromLong(sum);
}

static PyMethodDef PrimeMethods[] = {
    {"sum_primes", sum_primes, METH_VARARGS, "Sum primes up to N"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef prime_module = {
    PyModuleDef_HEAD_INIT,
    "prime",
    "Prime functions in C",
    -1,
    PrimeMethods
};

PyMODINIT_FUNC PyInit_prime(void) {
    return PyModule_Create(&prime_module);
}
