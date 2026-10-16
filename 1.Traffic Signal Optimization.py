#include <stdlib.h>
#include <limits.h>

// Define a structure to hold both the value and the minimum up to this node
typedef struct {
    int val;
    int min;
} Node;

typedef struct {
    Node* data;
    int topIndex;
    int capacity;
} MinStack;

/** Initializes the stack object */
MinStack* minStackCreate() {
    MinStack* obj = (MinStack*)malloc(sizeof(MinStack));
    obj->capacity = 20000; // Choose a safe default capacity based on constraints
    obj->data = (Node*)malloc(obj->capacity * sizeof(Node));
    obj->topIndex = -1;
    return obj;
}

/** Pushes the element val onto the stack */
void minStackPush(MinStack* obj, int val) {
    // If the capacity is reached, reallocate more memory
    if (obj->topIndex >= obj->capacity - 1) {
        obj->capacity *= 2;
        obj->data = (Node*)realloc(obj->data, obj->capacity * sizeof(Node));
    }
    
    obj->topIndex++;
    obj->data[obj->topIndex].val = val;
    
    // If it's the first element, it is the minimum.
    // Otherwise, calculate the minimum between the current val and the previous minimum.
    if (obj->topIndex == 0) {
        obj->data[obj->topIndex].min = val;
    } else {
        int currentMin = obj->data[obj->topIndex - 1].min;
        obj->data[obj->topIndex].min = (val < currentMin) ? val : currentMin;
    }
}

/** Removes the element on the top of the stack */
void minStackPop(MinStack* obj) {
    if (obj->topIndex >= 0) {
        obj->topIndex--;
    }
}

/** Gets the top element of the stack */
int minStackTop(MinStack* obj) {
    return obj->data[obj->topIndex].val;
}

/** Retrieves the minimum element in the stack */
int minStackGetMin(MinStack* obj) {
    return obj->data[obj->topIndex].min;
}

/** Frees the memory allocated for the stack */
void minStackFree(MinStack* obj) {
    free(obj->data);
    free(obj);
}
