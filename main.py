import os

# Function to create a .cpp file with a code template
def generate_cpp_file(task_name, include_segment_tree=False):
    cpp_code = R"""
#include <bits/stdc++.h>
using namespace std;

// Input/output management
void setIO(int argc, char* argv[]) {
    std::ios_base::sync_with_stdio(0); std::cin.tie(0);
    if (argc > 1) {
        // Reading from "in.txt" and writing to "out.txt"
        freopen("in.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
    }
}


#define ALL(v) v.begin(),v.end()
#define LB(v, i) lower_bound(ALL(v), i)
#define UB(v, i) upper_bound(ALL(v), i)

// Data types for convenience
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef unsigned long long ull;
typedef vector<vector<int>> vvi;
typedef vector<vector<ll>> vvl; 
typedef set<int> seti;

template <class T> 
using pqueue = priority_queue<T, vector<T>, greater<T>>;

// Iteration
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FORI(i, a) FOR(i, 0, a)
#define FOREV(i, a, b) for (int i = (b)-1; i >= (a); --i)
#define FOREVI(i, a) FOREV(i, 0, a)

// helpers
template<typename T>
bool even(T& val) { return val % 2 == 0; }

template<typename T>
bool odd(T& val) { return !even(val); }

template<typename T>
vector<T> readvt(int n)
{
    vector<T> r(n);
    int index = 0;
    while(index < n)
    {
        cin >> r[index];
        ++index;
    }
    return r;
}

template<typename T>
vector<vector<T>> readvvt(int n, int m) { 
    vector<vector<T>> r(n);
    for (int i = 0; i < n; ++i)
    {
        r[i] = readvt<T>(m);
    }
    return r;
}

vs readvs(int n) { return readvt<string>(n); }
vi readvi(int n) { return readvt<int>(n); }
vll readvl(int n) { return readvt<ll>(n); }
vvi readvvi(int n, int m) { return readvvt<int>(n, m); }
vvl readvvl(int n, int m) { return readvvt<ll>(n, m); }
seti getseti(vi& v) { 
    seti res; 
    for (auto num: v) res.insert(num);
    return res;
}

""" 

    # Segment Tree code if needed
    if include_segment_tree:
        cpp_code += R"""
template<typename T>
struct Node
{
    T max = std::numeric_limits<T>::min();
    T min = std::numeric_limits<T>::max();
    T sum = 0;
    int l = 0;
    int r = 0;
    std::unique_ptr<Node<T>> left = nullptr;
    std::unique_ptr<Node<T>> right = nullptr;
};

template<typename T>
using NodePtr = std::unique_ptr<Node<T>>;

template<typename T>
using NodePtr = std::unique_ptr<Node<T>>;

template<typename T>
class SegmentTree {
public:
    SegmentTree(int l, int r) {
        root = buildTree(l, r);
    }

    void update(int index, T value) {
        updatePath(root, index, value);
    }

    T getMax(int from, int to) {
        return getMax(root, from, to);
    }

    T getMin(int from, int to) {
        return getMin(root, from, to);
    }

    T getSum(int from, int to) {
        return getSum(root, from, to);
    }

private:
    NodePtr<T> root;

    NodePtr<T> buildTree(int l, int r) {
        if (l > r) {
            return nullptr;
        }
        auto node = std::make_unique<Node<T>>();
        node->l = l;
        node->r = r;
        
        if (l == r) {
            return node;
        }

        int mid = l + (r - l) / 2;
        node->left = buildTree(l, mid);
        node->right = buildTree(mid + 1, r);
        return node;
    }

    void updatePath(NodePtr<T>& current, int index, T value) {
        if (current == nullptr) {
            return;
        }

        if (current->r < index || current->l > index) {
            return;
        }

        if (current->l == current->r && current->l == index) {
            current->max = value;
            current->min = value;
            current->sum = value;
            return;
        }

        updatePath(current->left, index, value);
        updatePath(current->right, index, value);

        auto& left = current->left;
        auto& right = current->right;

        current->max = std::max(left ? left->max : std::numeric_limits<T>::min(),
                                right ? right->max : std::numeric_limits<T>::min());
        current->min = std::min(left ? left->min : std::numeric_limits<T>::max(),
                                right ? right->min : std::numeric_limits<T>::max());
        current->sum = (left ? left->sum : 0) + (right ? right->sum : 0);
    }

    T getMax(const NodePtr<T>& current, int from, int to) {
        if (current == nullptr) {
            return std::numeric_limits<T>::min();
        }

        if (current->r < from || current->l > to) {
            return std::numeric_limits<T>::min();
        }

        if (current->l >= from && current->r <= to) {
            return current->max;
        }

        T leftMax = getMax(current->left, from, to);
        T rightMax = getMax(current->right, from, to);
        return std::max(leftMax, rightMax);
    }

    T getMin(const NodePtr<T>& current, int from, int to) {
        if (current == nullptr) {
            return std::numeric_limits<T>::max();
        }

        if (current->r < from || current->l > to) {
            return std::numeric_limits<T>::max();
        }

        if (current->l >= from && current->r <= to) {
            return current->min;
        }

        T leftMin = getMin(current->left, from, to);
        T rightMin = getMin(current->right, from, to);
        return std::min(leftMin, rightMin);
    }

    T getSum(const NodePtr<T>& current, int from, int to) {
        if (current == nullptr) {
            return 0;
        }

        if (current->r < from || current->l > to) {
            return 0;
        }

        if (current->l >= from && current->r <= to) {
            return current->sum;
        }

        T leftSum = getSum(current->left, from, to);
        T rightSum = getSum(current->right, from, to);
        return leftSum + rightSum;
    }
};
"""
        
    cpp_code += """
// your solution here
void solution()
{
    int n;
    cin >> n;

    cout << n << endl;
    
    // your solution here
}

int main(int argc, char* argv[]) {
    // Set input/output from file if arguments are passed
    setIO(argc, argv);

    int t;
    cin >> t;
    while (t--)
    {
        solution();
    }
    return 0;
}
"""
    
    # Create a file with the specified name
    file_name = f"{task_name}.cpp"
    with open(file_name, "w") as f:
        f.write(cpp_code.strip())

    print(f"File '{file_name}' was successfully created! compile and run: ")
    print(f"g++ -g {file_name} && ./a.out -stub")

# Main function to get the task name and whether to include segment tree
if __name__ == "__main__":
    task_name = input("Enter the task name: ")
    include_segment_tree = input("Need to include advanced algos (segment trees/..): (y/n, default n - just skip enter) ").strip().lower()
    if include_segment_tree == '' or include_segment_tree == 'n':
        include_segment_tree = False
    else:
        include_segment_tree = True
    generate_cpp_file(task_name, include_segment_tree)