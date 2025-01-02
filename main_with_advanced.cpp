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


#include <bits/stdc++.h>
#include <limits>

template<typename T>
struct Node
{
    T max = std::numeric_limits<T>::min();
    T min = std::numeric_limits<T>::max();
    T sum = 0;
};

template<typename T>
class SegmentTree {
public:
    SegmentTree(const std::vector<T>& data) {
        n = data.size();
        tree.resize(4 * n, Node<T>());
        buildTree(data, 0, 0, n - 1);
    }

    void update(int index, T value) {
        updatePath(0, 0, n - 1, index, value);
    }

    T getMax(int from, int to) const {
        return getMaxQuery(0, 0, n - 1, from, to);
    }

    T getMin(int from, int to) const {
        return getMinQuery(0, 0, n - 1, from, to);
    }

    T getSum(int from, int to) const {
        return getSumQuery(0, 0, n - 1, from, to);
    }

private:
    std::vector<Node<T>> tree;
    int n;

    void buildTree(const std::vector<T>& data, int node, int l, int r) {
        if (l == r) {
            tree[node].max = data[l];
            tree[node].min = data[l];
            tree[node].sum = data[l];
            return;
        }

        int mid = l + (r - l) / 2;
        int leftChild = 2 * node + 1;
        int rightChild = 2 * node + 2;

        buildTree(data, leftChild, l, mid);
        buildTree(data, rightChild, mid + 1, r);

        tree[node].max = std::max(tree[leftChild].max, tree[rightChild].max);
        tree[node].min = std::min(tree[leftChild].min, tree[rightChild].min);
        tree[node].sum = tree[leftChild].sum + tree[rightChild].sum;
    }

    void updatePath(int node, int l, int r, int index, T value) {
        if (l == r) {
            tree[node].max = value;
            tree[node].min = value;
            tree[node].sum = value;
            return;
        }

        int mid = l + (r - l) / 2;
        int leftChild = 2 * node + 1;
        int rightChild = 2 * node + 2;

        if (index <= mid) {
            updatePath(leftChild, l, mid, index, value);
        } else {
            updatePath(rightChild, mid + 1, r, index, value);
        }

        tree[node].max = std::max(tree[leftChild].max, tree[rightChild].max);
        tree[node].min = std::min(tree[leftChild].min, tree[rightChild].min);
        tree[node].sum = tree[leftChild].sum + tree[rightChild].sum;
    }

    T getMaxQuery(int node, int l, int r, int from, int to) const {
        if (to < l || from > r) {
            return std::numeric_limits<T>::min();
        }

        if (from <= l && r <= to) {
            return tree[node].max;
        }

        int mid = l + (r - l) / 2;
        int leftChild = 2 * node + 1;
        int rightChild = 2 * node + 2;

        T leftMax = getMaxQuery(leftChild, l, mid, from, to);
        T rightMax = getMaxQuery(rightChild, mid + 1, r, from, to);
        return std::max(leftMax, rightMax);
    }

    T getMinQuery(int node, int l, int r, int from, int to) const {
        if (to < l || from > r) {
            return std::numeric_limits<T>::max();
        }

        if (from <= l && r <= to) {
            return tree[node].min;
        }

        int mid = l + (r - l) / 2;
        int leftChild = 2 * node + 1;
        int rightChild = 2 * node + 2;

        T leftMin = getMinQuery(leftChild, l, mid, from, to);
        T rightMin = getMinQuery(rightChild, mid + 1, r, from, to);
        return std::min(leftMin, rightMin);
    }

    T getSumQuery(int node, int l, int r, int from, int to) const {
        if (to < l || from > r) {
            return 0;
        }

        if (from <= l && r <= to) {
            return tree[node].sum;
        }

        int mid = l + (r - l) / 2;
        int leftChild = 2 * node + 1;
        int rightChild = 2 * node + 2;

        T leftSum = getSumQuery(leftChild, l, mid, from, to);
        T rightSum = getSumQuery(rightChild, mid + 1, r, from, to);
        return leftSum + rightSum;
    }
};

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