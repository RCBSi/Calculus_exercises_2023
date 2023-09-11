s = 'inverse%20%5Cbegin%7Bpmatrix%7D%5Ccos%5Cleft(%5Ctheta%5Cright)%20%5Csin%5Cleft(%5Cphi%5Cright)%261%261%5C%5C%200%261%260%5C%5C%200%260%261%5Cend%7Bpmatrix%7D?or=input'

def html_to_human(s):
    o1 = []
    i0 = 0
    while i0 < len(s):
        if s[i0] == '%':
            o1.append(chr(int(s[i0+1:i0+3], 16)))
            i0 += 3
        else: 
            o1.append(s[i0])
            i0 += 1
    return o1

def human_to_html(o1):
    s1 = ''
    i0 = 0
    while i0 < len(o1):
        if ord(o1[i0]) in range(ord('a'), ord('z')+1):
            s1 += o1[i0]
            i0 += 1
        elif ord(o1[i0]) in range(ord('A'), ord('Z')+1):
            s1 += o1[i0]
            i0 += 1
        elif o1[i0] in ['0','(','1','2','3','4','5','6','7','8','9',')']:
            s1 += o1[i0]
            i0 += 1
        elif o1[i0] == '?':
            s1 += o1[i0:]
            return s1
#        elif o1[i0] == '_':
#            return '%5F'
        else: 
            s1 += '%'
            s1 += hex(ord(o1[i0]))[2:].upper()
            i0 += 1
    return s1

#print(s)
#print(html_to_human(s))
#print(human_to_html(html_to_human(s)) == s)
#print(html_to_human(s))
#print(human_to_html('inverse \\begin{pmatrix}\cos\left(\\theta\\right) \sin\left(\phi\\right)&-r\sin(\\theta)\sin(\phi)&r\cos(\\theta)\cos(\phi)\\\sin(\\theta)\sin(\phi)&r\cos(\\theta)\sin(\phi)&r\sin(\\theta)\cos(\phi)\\ 0&0&1\end{pmatrix}?or=input'))
#print(human_to_html('inverse \\begin{pmatrix}\\cos\\left(\\theta\\right) \\sin\\left(\\phi\\right)&-r\\sin(\\theta)\\sin(\\phi)&r\\cos(\\theta)\\cos(\\phi)\\\\\\sin(\\theta)\\sin(\\phi)&r\\cos(\\theta)\\sin(\\phi)&r\\sin(\\theta)\\cos(\\phi)\\\\ 0&0&1\\end{pmatrix}?or=input'))
#print(human_to_html('inverse \\begin{pmatrix}\\cos\\left(\\theta\\right) \\sin\\left(\\phi\\right)&-r\\sin(\\theta)\\sin(\\phi)&r\\cos(\\theta)\\cos(\\phi)\\\\\\sin(\\theta)\\sin(\\phi)&r\\cos(\\theta)\\sin(\\phi)&r\\sin(\\theta)\\cos(\\phi)\\\\ \\cos(\\theta)&0&- r \\sin(\\phi)\\end{pmatrix}?or=input'))
#print(human_to_html('inverse \\begin{pmatrix}\\cos(\\phi_1)  & - r \\sin(\\phi_1) & 0 \\\\\\sin(\\phi_1) \\cos(\\phi_2) &  r \\cos(\\phi_1)  \\cos(\\phi_2) & -r \\sin(\\phi_1) \\sin(\\phi_2) \\\\ \\sin(\\phi_1) \\sin(\\phi_2) & r \\cos(\\phi_1) \\sin(\\phi_2) & r \\sin(\\phi_1) \\cos(\\phi_2) \\end{pmatrix}?or=input'))
pre_cos_sin_constant = '' # could be '\'
pcs = pre_cos_sin_constant
spherical_laplacian_dict = {
    'c_1' : pcs + 'cos\(\phi_1\)', 
    's_1' : pcs + 'sin\(\phi_1\)', 
    'c_2' : pcs + 'cos\(\phi_2\)', 
    's_2' : pcs + 'sin\(\phi_2\)', 
    '(':'left(',
    ')':'right('
    }

string1 = 'c_1 c_2'# \partial_0 + s_1 c_2 \partial_1 \partial_0 - \dfrac{s_1 c_2}{r} \partial_1 + \dfrac{c_1 c_2}{r} \partial_0 \partial_1 + \dfrac{c_1}{s^2_1}\dfrac{s_2}{r} \partial_2 - \dfrac{s_2}{r s_1} \partial_1 \partial_2'
for x in spherical_laplacian_dict:
    string1 = string1.replace(x, spherical_laplacian_dict[x])

print('https://www.symbolab.com/solver/simplify%20'+human_to_html(' '+string1+'\dfrac{s_1 c_2}{r}')+'?or=input')
#https://www.symbolab.com/solver/simplify_cos(%5Cphi_1)%20cos(%5Cphi_2)/simplify%20cos%5E%7B2%7D%5Cleft(x%5Cright)?or=input
#https://www.symbolab.com/solver/simplify%20cos(%5Cphi%5F1)%20cos(%5Cphi%5F2)%20%5Cpartial%5F0%20%2B%20sin(%5Cphi%5F1)%20cos(%5Cphi%5F2)%

https://www.symbolab.com/solver/step-by-step/simplify%20cos%5E%7B2%7D%5Cleft(%5Cphi_%7B1%7D%5Cright)%20%2B%20sin%5E%7B2%7D%5Cleft(%5Cphi_%7B1%7D%5Cright)?or=input

https://www.symbolab.com/solver/simplify%20%20cos%5Cleft(%5Cphi%5F1%5Cright(%20cos%5Cleft(%5Cphi%5F2%5Cright(%5
https://www.symbolab.com/solver/simplify%20%20cos%5Cleft(%5Cphi_1%5Cright(%20cos%5Cleft(%5Cphi_2%5Cright(%5Cdfrac%7Bs_1%20c_2%7D%7Br%7D/simplify%20cos%5Cleft(phi_%7B1%7D%5Cright)?or=input

''.join(html_to_human('https://www.symbolab.com/solver/step-by-step/simplify%20cos%5E%7B2%7D%5Cleft(%5Cphi_%7B1%7D%5Cright)%20%2B%20sin%5E%7B2%7D%5Cleft(%5Cphi_%7B1%7D%5Cright)?or=input'))

'https://www.symbolab.com/solver/step-by-step/simplify cos^{2}\\left(\\phi_{1}\\right) + sin^{2}\\left(\\phi_{1}\\right)?or=input'

human_to_html('cos^{2}\\left(\\phi_{1}\\right) + sin^{2}\\left(\\phi_{1}\\right)')
cos%5E%7B2%7D%5Cleft(%5Cphi_%7B1%7D%5Cright)%20%2B%20sin%5E%7B2%7D%5Cleft(%5Cphi_%7B1%7D%5Cright)?or=input
cos%5E%7B2%7D%5Cleft(%5Cphi%5F%7B1%7D%5Cright)%20%2B%20sin%5E%7B2%7D%5Cleft(%5Cphi%5F%7B1%7D%5Cright)'


