// on Mac OS
#include <Python/Python.h>
//on Linux
//#include <Python.h>

/*gcc -shared -o sample.so sample.c -framework Python*/

static PyObject* supermodule(PyObject* self)
{
    return Py_BuildValue("s", "Message form c extention");

}

static char supermodule_docs[] =
"supermodule(  ): Some info\n";

static PyMethodDef supermodule_funcs[] = {
    {"supermodule", (PyCFunction)supermodule,
        METH_NOARGS, supermodule_docs},
    {NULL}

};

void initsupermodule(void)
{
    Py_InitModule3("supermodule", supermodule_funcs,
            "Super module extention");

}
