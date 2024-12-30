import os

# Function to create a .cpp file with a code template
def generate_cpp_file(task_name):
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
#define first_eg(v, i) lower_bound(ALL(v), i)
#define first_g(v, i) upper_bound(ALL(v), i)

// Data types for convenience
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef vector<vector<int>> vvi;
typedef vector<vector<ll>> vvl; 
typedef set<int> seti;

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

# Main function to get the task name
if __name__ == "__main__":
    task_name = input("Enter the task name: ")
    generate_cpp_file(task_name)
