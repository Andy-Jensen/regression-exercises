def scale_data(t, v, te):
    ss_scaler = sklearn.preprocessing.StandardScaler()
    ss_scaler.fit(t)
    
    st=train_scaled = ss_scaler.transform(t)
    sv=validate_scaled = ss_scaler.transform(v)
    ste=test_scaled = ss_scaler.transform(te)

    return st, sv, ste