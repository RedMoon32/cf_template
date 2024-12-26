import os

# Function to create a .cpp file with a code template
def generate_cpp_file(task_name):
    cpp_code = f"""
#include <bits/stdc++.h>
using namespace std;

// Data types for convenience
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pii> vpii;

#define ALL(v) v.begin(),v.end()

// Input/output management
void setIO(int argc, char* argv[]) {{
    std::ios_base::sync_with_stdio(0); std::cin.tie(0);
    if (argc > 1) {{
        // Reading from "in.txt" and writing to "out.txt"
        freopen("in.txt", "r", stdin);
        freopen("out.txt", "w", stdout);
    }}
}}

vi readv(int n)
{{
    vi r(n);
    int index = 0;
    while(index < n)
    {{
        cin >> r[index];
        ++index;
    }}
    return r;
}}

int main(int argc, char* argv[]) {{
    // Set input/output from file if arguments are passed
    setIO(argc, argv);

    // Your logic here
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;

    return 0;
}}
    """

    # Create a file with the specified name
    file_name = f"{task_name}.cpp"
    with open(file_name, "w") as f:
        f.write(cpp_code.strip())

    print(f"File '{file_name}' was successfully created!")

# Main function to get the task name
if __name__ == "__main__":
    task_name = input("Enter the task name: ")
    generate_cpp_file(task_name)
