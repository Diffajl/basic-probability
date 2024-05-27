import streamlit as st
import itertools, math

class Probability:
    def __init__(self, data):
        self.data = data

    def permutasi_sederhana(self):
        perm = itertools.permutations(self.data)
        st.write("Susunan Permutasi:")

        for p in perm:
            st.write(p)

        nilai = math.factorial(len(self.data))
        st.write("Nilai Permutasi:")
        # st.latex(rf"{len(self.data)}P{self.data[1]} = \frac{{{len(self.data)}!}}{{({self.data[0]}-{self.data[1]})!}}")
        st.latex(rf'{len(self.data)}! = {nilai}')
        # st.write(nilai)

    def permutasi_sot(self, data):
        perm1 = itertools.permutations(data, int(self.data[1]))
        perm2 = itertools.permutations(range(int(self.data[0])), int(self.data[1]))
        
        st.write("Susunan Permutasi:")
        for p in perm1:
            st.write(p)
        
        st.write("Nilai Permutasi:")

        st.latex(rf"{len(data)}P{self.data[1]} = \frac{{{len(data)}!}}{{({self.data[0]}-{self.data[1]})!}} = {len(tuple(perm2))}")
        # st.write(len(tuple(perm2)))

    def kombinasi_sederhana(self, data):
        comb1 = itertools.combinations(data, int(self.data[1]))
        comb2 = itertools.combinations(range(int(self.data[0])), int(self.data[1]))
        st.write("Susunan kombinasi: ")
        for c in comb1:
            st.write(c)

        st.write("Nilai Combinasi: ")
        st.latex(rf"{len(data)}C{self.data[1]} = \frac{{{len(data)}!}}{{({self.data[0]}-{self.data[1]})! \times {self.data[1]}!}} = {len(tuple(comb2))}")


def main():
    st.markdown("<h1 style='text-align: center;'>Probabilitas Dasar</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Apa itu Permutasi?</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Permutasi adalah pengaturan urutan penyusunan sekumpulan nilai objek unik(Tidak mengandung duplikasi). Permutasi dari sekumpulan b objek dapat diformulasikan sebagai faktorial dari n</p>", unsafe_allow_html=True)
    st.latex(r'n! = n \times (n-1) \times (n-2) \times \ldots \times 3 \times 2 \times 1')
    st.markdown("<p style='text-align:center;'>Kasus Khusus:</p>", unsafe_allow_html=True)
    st.latex(r'0! = 1')
    st.markdown("<p style='text-align: center;'>Permutasi pada pengaturan urutan penyusunan sejumlah r objek yang diambil dari sekumpulan n objek unik dapat diformulasikan sebagai berikut</p>", unsafe_allow_html=True)
    st.latex(r'nPr = \frac{n!}{(n-r)!}')
    st.markdown("<p style='text-align: center;'>dengan r <= n</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Permutasi Duplikasi</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Permutasi yang melibatkan kemunculan beberapa kali objek sejenis dapat diformulasikan sebagai berikut</p>", unsafe_allow_html=True)

    st.latex(r'\frac{n!}{n1! \times n2! \times n3! \times ... \times Nk!}')
    st.markdown("<h2 style='text-align: center;'>Apa itu Kombinasi?</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Kombinasi adalah pemimihan sejumlah r objek dari sekumpuln N objek tanpa memperhatikan urutan.</p>", unsafe_allow_html=True)
    st.latex(r'nCr = \frac{n!}{(n-r)! \times r!}')
    st.markdown("<p style='text-align: center;'>dengan r <= n</p>", unsafe_allow_html=True)

    menu = st.selectbox("Masukan menu:", ("Permutasi Sederhana", "Permutasi Pada Sejumlah Objek Tertentu", "Kombinasi"))

    match menu:
        case "Permutasi Sederhana":
            data = st.text_input("Masukan data").split()
            data = [str(x) for x in data]
            if data:
                prob = Probability(data)
                prob.permutasi_sederhana()

        case "Permutasi Pada Sejumlah Objek Tertentu":
            data = st.text_input("Masukan data:").split()
            data = [str(x) for x in data]
            n = st.text_input("Masukan n:")
            r = st.text_input("Masukan r:")
            if n and r and data:
                prob = Probability(list([n, r]))
                prob.permutasi_sot(data)

        case "Kombinasi":
            data = st.text_input("Masukan data:").split()
            data = [str(x) for x in data]
            n = st.text_input("Masukan n:")
            r = st.text_input("Masukan r:")
            if n and r:
                prob = Probability(list([n, r]))
                prob.kombinasi_sederhana(data)


if __name__ == "__main__":
    main()
