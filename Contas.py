import streamlit as st

st.title("Gestor de Despesas")

# Tabs para as seções
tab1, tab2, tab3 = st.tabs(["Mensal", "Trimestral", "Anual"])

with tab1:
    st.header("Despesas Mensais")
    
    # Despesas fixas mensais
    casa = st.number_input("Casa", value=0.0, step=0.01)
    agua = st.number_input("Água", value=0.0, step=0.01)
    luz = st.number_input("Luz", value=0.0, step=0.01)
    telemoveis = st.number_input("Telemóveis", value=0.0, step=0.01)
    atelier = st.number_input("Atelier", value=0.0, step=0.01)
    feira = st.number_input("Feira", value=0.0, step=0.01)
    catarina = st.number_input("Catarina", value=0.0, step=0.01)
    ginasticas = st.number_input("Ginásticas", value=0.0, step=0.01)
    seguranca_social = st.number_input("Segurança Social", value=0.0, step=0.01)
    
    # Seção de extras mensais
    st.subheader("Extras Mensais")
    if 'monthly_extras' not in st.session_state:
        st.session_state.monthly_extras = []
    
    num_monthly_extras = st.number_input("Número de extras mensais", min_value=0, value=len(st.session_state.monthly_extras), step=1)
    
    # Ajustar a lista de extras
    while len(st.session_state.monthly_extras) < num_monthly_extras:
        st.session_state.monthly_extras.append({"name": "", "amount": 0.0})
    if len(st.session_state.monthly_extras) > num_monthly_extras:
        st.session_state.monthly_extras = st.session_state.monthly_extras[:num_monthly_extras]
    
    monthly_extras_total = 0.0
    for i in range(num_monthly_extras):
        with st.container():
            col1, col2 = st.columns(2)
            st.session_state.monthly_extras[i]["name"] = col1.text_input(f"Nome do extra {i+1}", value=st.session_state.monthly_extras[i]["name"], key=f"monthly_extra_name_{i}")
            st.session_state.monthly_extras[i]["amount"] = col2.number_input(f"Valor do extra {i+1}", value=st.session_state.monthly_extras[i]["amount"], step=0.01, key=f"monthly_extra_amount_{i}")
            monthly_extras_total += st.session_state.monthly_extras[i]["amount"]
    
    # Cálculo do total mensal
    total_mensal = (casa + agua + luz + telemoveis + atelier + feira + catarina + ginasticas + seguranca_social + monthly_extras_total)
    st.write(f"**Total Mensal:** {total_mensal:.2f} €")

with tab2:
    st.header("Despesas Trimestrais")
    
    # Despesas fixas trimestrais
    contabilista_trim = st.number_input("Contabilista (Trimestral)", value=0.0, step=0.01)
    
    # Seção de extras trimestrais
    st.subheader("Extras Trimestrais")
    if 'quarterly_extras' not in st.session_state:
        st.session_state.quarterly_extras = []
    
    num_quarterly_extras = st.number_input("Número de extras trimestrais", min_value=0, value=len(st.session_state.quarterly_extras), step=1)
    
    # Ajustar a lista de extras
    while len(st.session_state.quarterly_extras) < num_quarterly_extras:
        st.session_state.quarterly_extras.append({"name": "", "amount": 0.0})
    if len(st.session_state.quarterly_extras) > num_quarterly_extras:
        st.session_state.quarterly_extras = st.session_state.quarterly_extras[:num_quarterly_extras]
    
    quarterly_extras_total = 0.0
    for i in range(num_quarterly_extras):
        with st.container():
            col1, col2 = st.columns(2)
            st.session_state.quarterly_extras[i]["name"] = col1.text_input(f"Nome do extra {i+1}", value=st.session_state.quarterly_extras[i]["name"], key=f"quarterly_extra_name_{i}")
            st.session_state.quarterly_extras[i]["amount"] = col2.number_input(f"Valor do extra {i+1}", value=st.session_state.quarterly_extras[i]["amount"], step=0.01, key=f"quarterly_extra_amount_{i}")
            quarterly_extras_total += st.session_state.quarterly_extras[i]["amount"]
    
    # Cálculo do total trimestral
    total_trimestral = (contabilista_trim + quarterly_extras_total)
    st.write(f"**Total Trimestral:** {total_trimestral:.2f} €")

with tab3:
    st.header("Despesas Anuais")
    
    # Despesas fixas anuais
    seguro = st.number_input("Seguro", value=0.0, step=0.01)
    iuc = st.number_input("IUC", value=0.0, step=0.01)
    contabilista_anual = st.number_input("Contabilista (Anual)", value=0.0, step=0.01)
    
    # Seção de extras anuais
    st.subheader("Extras Anuais")
    if 'annual_extras' not in st.session_state:
        st.session_state.annual_extras = []
    
    num_annual_extras = st.number_input("Número de extras anuais", min_value=0, value=len(st.session_state.annual_extras), step=1)
    
    # Ajustar a lista de extras
    while len(st.session_state.annual_extras) < num_annual_extras:
        st.session_state.annual_extras.append({"name": "", "amount": 0.0})
    if len(st.session_state.annual_extras) > num_annual_extras:
        st.session_state.annual_extras = st.session_state.annual_extras[:num_annual_extras]
    
    annual_extras_total = 0.0
    for i in range(num_annual_extras):
        with st.container():
            col1, col2 = st.columns(2)
            st.session_state.annual_extras[i]["name"] = col1.text_input(f"Nome do extra {i+1}", value=st.session_state.annual_extras[i]["name"], key=f"annual_extra_name_{i}")
            st.session_state.annual_extras[i]["amount"] = col2.number_input(f"Valor do extra {i+1}", value=st.session_state.annual_extras[i]["amount"], step=0.01, key=f"annual_extra_amount_{i}")
            annual_extras_total += st.session_state.annual_extras[i]["amount"]
    
    # Cálculo do total anual
    total_anual = (seguro + iuc + contabilista_anual + annual_extras_total)
    st.write(f"**Total Anual:** {total_anual:.2f} €")
