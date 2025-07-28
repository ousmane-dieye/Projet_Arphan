import MySQLdb

try:
    conn = MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        passwd="ton_mdp_ici",
        db="site_arphan"
    )
    print("Connexion réussie !")
    conn.close()
except Exception as e:
    print("Erreur de connexion :", e)
