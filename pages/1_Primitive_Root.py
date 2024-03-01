import streamlit as st

def is_primitive(q,g):
    def mod_pow(base, exponent, modulos):
        result = 1
        base %= modulos
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulos
            exponent //= 2
            base = (base * base) % modulos
        return result
        
    primitive_roots = []
    output = []
    
    for i in range(1, q):
        tests = []
        current_output = f"{i}^1 mod {q} = {mod_pow(i, 1, q)}|\n"
        tests.append(mod_pow(i, 1, q))
        for j in range(2, q):
            test = mod_pow(i, j, q)
            if test in tests:
                break
            tests.append(test)
            current_output += f"{i}^{j} mod {q} = {test}|\n"
        if len(tests) == q - 1:
            primitive_roots.append(i)
            current_output = current_output[:-1] + f" ==> {i} is primitive root of {q}|\n"
        output.append(current_output)
    st.write("\n".join(output))
    
    is_primitive = g in primitive_roots
    if is_primitive == False:
        st.write(f"{g} is NOT primitive root of {q} - List of Primitive roots: {primitive_roots}")
    else:
        st.write(f"{g} is primitive root: {is_primitive} {primitive_roots}")

if __name__ =="__main__":
    st.write("# Welcome To Primitive Root🔒🔒🔒")
    q = st.number_input("Enter a prime number", step = 1)
    g = st.number_input("Guess a primitive root of prime number", step = 1)
    
    if st.button("Encrypt!"):
        if q > 1:
            for i in range(2, int(q / 2)+1):
                if (q % i) == 0:
                    st.write(f"{q} is not a prime number!!")
                    break
            else:
                is_primitive(q, g)
