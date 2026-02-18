import streamlit as st
from groq import Groq

st.set_page_config(page_title="App-Frigorifero", page_icon="🍳")

# Palloncini per Martina!
if 'balloons' not in st.session_state:
    st.balloons()
    st.session_state['balloons'] = True

st.title("👨‍🍳 Lo Chef di Martina")
st.write("Inserisci gli ingredienti e creerò una ricetta magica!")

# Sidebar per la chiave Groq
st.sidebar.header("Configurazione")
api_key_input = st.sidebar.text_input("Inserisci la tua GROQ API Key (gsk_...)", type="password")

ingredienti = st.text_input("Cosa abbiamo in frigo?", placeholder="es: uova, pancetta, pasta")

if st.button("Genera Ricetta ✨"):
    if not api_key_input:
        st.error("Manca la chiave API nella barra laterale!")
    elif ingredienti:
        try:
            client = Groq(api_key=api_key_input.strip())
            
            with st.spinner('Cucinando per Martina...'):
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "user", "content": f"Sei uno chef stellato. Inventa una ricetta con: {ingredienti}. Dai un nome al piatto, elenca i passaggi e chiudi con una dedica dolce per Martina."}
                    ],
                )
                
                st.success("Ecco la tua ricetta!")
                st.markdown(completion.choices[0].message.content)
        except Exception as e:
            st.error(f"Errore: {e}")
    else:
        st.warning("Scrivi almeno un ingrediente!")