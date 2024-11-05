import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
day_df = pd.read_csv("day_df.csv")
hours_df = pd.read_csv("hours_df.csv")

with st.sidebar:
        st.image("BIKERS.png",width=300)
        st.title("THE BIKERS SHARING")
        
        option = st.selectbox(
        "Pilih data yang ingin ditampilkan",
        ("Banyak pesepeda yang teregistrasi dan tidak(casual)",
         "Hari pesepeda meningkat",
         "pengaruh musim dan cuaca "
    ),
        ) 
if option == "Banyak pesepeda yang teregistrasi dan tidak(casual)":
        pengguna = day_df[['casual','registered']].sum()
        st.subheader("Banyak pesepeda casual dan register(perhari)")

        fig, ax = plt.subplots(figsize=(10,5))
        sns.barplot(x=pengguna.index, y=pengguna.values, palette='viridis', ax=ax)
        ax.set_title("Jumlah Pengguna Sepeda")
        ax.set_xlabel("Tipe Pengguna")
        ax.set_ylabel("Jumlah Pengguna")

        # Display the plot in Streamlit
        st.pyplot(fig)

        pengguna = hours_df[['casual','registered']].sum()
        st.subheader("Banyak pesepeda casual dan register(perjam)")


        fig, ax = plt.subplots(figsize=(10,5))
        sns.barplot(x=pengguna.index, y=pengguna.values, palette='viridis', ax=ax)
        ax.set_title("Jumlah Pengguna Sepeda")
        ax.set_xlabel("Tipe Pengguna")
        ax.set_ylabel("Jumlah Pengguna")
        st.pyplot(fig)

elif option == "Hari pesepeda meningkat":
        st.subheader("Banyak pesepeda (perjam)")

        counts = hours_df[['holiday', 'weekday']].value_counts().reset_index(name='count')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=counts, x='count', y='weekday', hue='holiday', orient='h', ax=ax)
        ax.set_title('Jumlah Berdasarkan Hari Libur dan Hari Kerja')
        ax.set_xlabel('Jumlah')
        ax.set_ylabel('Hari dalam Minggu (0=Senin, ..., 6=Minggu)')
        ax.legend(title='Libur (1=Holiday, 0=No)')

        # Tampilkan plot di Streamlit
        st.pyplot(fig)

        st.subheader("Banyak pesepeda (perhari)")

        counts = day_df[['holiday', 'weekday']].value_counts().reset_index(name='count')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=counts, x='count', y='weekday', hue='holiday', orient='h', ax=ax)
        ax.set_title('Jumlah Berdasarkan Hari Libur dan Hari Kerja')
        ax.set_xlabel('Jumlah')
        ax.set_ylabel('Hari dalam Minggu (0=Senin, ..., 6=Minggu)')
        ax.legend(title='Libur (1=Holiday, 0=No)')

        # Tampilkan plot di Streamlit
        st.pyplot(fig)

elif option == "pengaruh musim dan cuaca ":
        st.subheader("Banyak pesepeda (perjam)")
        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
        casual_df = hours_df.groupby('cuaca').agg(casual=('casual', 'mean'))
        registered_df = hours_df.groupby('cuaca').agg(registered=('registered', 'mean'))
        sns.barplot(data=casual_df, x=casual_df.index, y='casual', ax=axs[0])
        axs[0].set_title('Rata-rata Pengguna Sepeda Casual')
        axs[0].set_xlabel('Cuaca')
        axs[0].set_ylabel('Rata-rata Pengguna')

        # Plot bar untuk pengguna registered
        sns.barplot(data=registered_df, x=registered_df.index, y='registered', ax=axs[1])
        axs[1].set_title('Rata-rata Pengguna Sepeda Registered')
        axs[1].set_xlabel('Cuaca')
        axs[1].set_ylabel('Rata-rata Pengguna')
        for ax in axs:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.2)
        st.pyplot(fig)

        st.subheader("Banyak pesepeda (perhari)")
        fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
        casual_df = day_df.groupby('cuaca').agg(casual=('casual', 'mean'))
        registered_df = day_df.groupby('cuaca').agg(registered=('registered', 'mean'))
        sns.barplot(data=casual_df, x=casual_df.index, y='casual', ax=axs[0])
        axs[0].set_title('Rata-rata Pengguna Sepeda Casual')
        axs[0].set_xlabel('Cuaca')
        axs[0].set_ylabel('Rata-rata Pengguna')

        # Plot bar untuk pengguna registered
        sns.barplot(data=registered_df, x=registered_df.index, y='registered', ax=axs[1])
        axs[1].set_title('Rata-rata Pengguna Sepeda Registered')
        axs[1].set_xlabel('Cuaca')
        axs[1].set_ylabel('Rata-rata Pengguna')
        for ax in axs:
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.2)
        st.pyplot(fig)
st.caption('Copyright (c) FHARAHBI 2024')