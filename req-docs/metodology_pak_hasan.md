## Metodology
<b>Pendahuluan</b>
<p align="justify">
Projek ini merupakan sistem deteksi performa siswa, yaitu aplikasi yang menggunakan AI untuk meningkatkan keterlibatan siswa dalam pembelajaran jarak jauh. Dalam analisis ini, kami mempertimbangkan enam metodologi pengembangan perangkat lunak, yaitu Waterfall, Parallel Development, Incremental Model, Spiral Model, Rapid Application Development (RAD), dan Agile (XP). Masing-masing metodologi memiliki kelebihan dan kekurangan, serta relevansi tersendiri dalam konteks proyek yang membutuhkan komponen AI, antarmuka pengguna yang intuitif, dan keterlibatan pengguna yang intensif.

1. **Waterfall**  
   **Kelebihan:**
   - Struktur yang sederhana dan mudah diikuti karena berurutan dari tahap satu ke tahap berikutnya, seperti analisis, desain, implementasi, pengujian, dan pemeliharaan.
   - Setiap tahap terdefinisi dengan baik, sehingga memudahkan tim dalam mengelola proyek dan mengontrol setiap langkah.
   - Cocok untuk projek yang memiliki persyaratan yang stabil dan sudah diketahui sejak awal, sehingga tidak perlu banyak perubahan di tengah jalan.

   **Kekurangan:**
   - Kurang fleksibel karena semua tahapan harus diselesaikan secara penuh sebelum melanjutkan ke tahap berikutnya, sehingga sulit untuk beradaptasi jika ada perubahan kebutuhan selama pengembangan.
   - Rentan terhadap keterlambatan feedback pengguna karena produk akhir baru bisa dilihat setelah seluruh proses selesai.
   - Tidak cocok untuk proyek yang membutuhkan feedback berkelanjutan atau penyesuaian seperti pengembangan AI, di mana iterasi dan penyempurnaan seringkali dibutuhkan.

   **Relevansi untuk projek ini:**
   Metode ini kurang ideal karena projek ini membutuhkan pengembangan yang responsif terhadap perubahan kebutuhan dan masukan pengguna, khususnya dalam fitur deteksi emosi yang memerlukan pengujian dan penyesuaian terus-menerus. Waterfall tidak mendukung fleksibilitas ini dengan baik.

2. **Parallel Development**  
   **Kelebihan:**
   - Proses pengembangan dapat dipercepat dengan membagi proyek menjadi beberapa sub-proyek yang dikerjakan secara bersamaan (paralel), seperti tim AI dan tim antarmuka pengguna yang bekerja secara terpisah.
   - Mengurangi jeda waktu antara tahap analisis dan pengiriman sistem karena beberapa komponen dapat dikembangkan bersamaan.

   **Kekurangan:**
   - Koordinasi dan integrasi antar sub-proyek bisa menjadi tantangan, terutama jika tim tidak terkoordinasi dengan baik atau jika ada ketergantungan antar modul.
   - Memerlukan perencanaan yang matang agar pada tahap akhir, integrasi sub-proyek tidak mengalami kendala teknis yang signifikan.

   **Relevansi untuk projek ini:**
   Parallel Development bisa dipertimbangkan jika komponen AI (deteksi emosi) dan antarmuka pengguna dikembangkan secara terpisah. Namun, integrasi antara kedua komponen ini bisa menjadi tantangan tersendiri, terutama karena antarmuka pengguna bergantung pada akurasi dan performa dari model AI.

3. **Incremental Model**  
   **Kelebihan:**
   - Memungkinkan tim untuk mengirimkan produk dengan fitur dasar terlebih dahulu, yang dapat digunakan dan diuji oleh pengguna. Fitur tambahan bisa dikembangkan secara bertahap di iterasi berikutnya.
   - Mendapatkan feedback pengguna secara cepat setelah produk dasar dirilis, yang membantu pengembangan iteratif dan penyempurnaan fitur.

   **Kekurangan:**
   - Versi awal mungkin belum lengkap, sehingga pengguna harus menunggu beberapa iterasi berikutnya untuk mendapatkan semua fitur yang diinginkan.
   - Fitur-fitur yang lebih kompleks mungkin harus ditunda hingga iterasi berikutnya, yang bisa menyebabkan jeda dalam ketersediaan fitur penuh.

   **Relevansi untuk projek ini:**
   Model ini cocok untuk proyek yang membutuhkan penyempurnaan secara bertahap, seperti pada projek ini, dengan Incremental Model, aplikasi dapat dimulai dengan fitur dasar deteksi emosi dan penerjemahan bahasa, kemudian diupdate untuk penambahan fitur kompleks seperti personalisasi soal atau analisis performa yang lebih mendalam.

4. **Spiral Model**  
   **Kelebihan:**
   - Spiral menggabungkan pendekatan iteratif dengan manajemen risiko, di mana setiap siklus fokus pada identifikasi dan mitigasi risiko utama.
   - Memungkinkan pengembangan prototipe secara bertahap, sehingga risiko teknis atau operasional dapat diidentifikasi lebih awal dan disesuaikan.

   **Kekurangan:**
   - Membutuhkan keahlian khusus dalam analisis risiko dan perencanaan, sehingga mungkin lebih rumit dan mahal dibandingkan model lain.
   - Kompleksitasnya membuat model ini kurang cocok untuk proyek dengan sumber daya terbatas.

   **Relevansi untuk projek ini:**
   Spiral cocok untuk proyek yang memiliki ketidakpastian tinggi dalam hal teknologi, seperti pengembangan AI. Namun, karena model ini lebih kompleks dan memerlukan manajemen risiko yang intensif, mungkin kurang cocok jika sumber daya terbatas. Proyek ini membutuhkan solusi yang lebih adaptif dan cepat untuk merespons umpan balik.

5. **Rapid Application Development (RAD)**  
   **Kelebihan:**
   - Mendorong pengembangan cepat melalui pembuatan prototipe yang dapat diuji dan ditinjau oleh pengguna. Feedback dapat diperoleh dengan cepat dan diperbaiki dalam iterasi berikutnya.
   - RAD cocok untuk proyek yang memerlukan penyesuaian berkelanjutan, sehingga pengembangan dapat berlangsung dengan iterasi singkat.

   **Kekurangan:**
   - Versi awal mungkin kurang stabil atau tidak memiliki semua fitur yang diperlukan, yang bisa mengganggu pengalaman pengguna.
   - Membutuhkan keterlibatan pengguna untuk memberikan feedback yang konsisten, yang bisa memperlambat proses jika pengguna tidak tersedia.

   **Relevansi untuk projek ini:**
   RAD bisa digunakan untuk mempercepat pengembangan pada projek ini, khususnya dalam hal prototyping fitur deteksi emosi. Namun, aplikasi ini membutuhkan stabilitas yang cukup tinggi karena berkaitan dengan analisis performa siswa, sehingga RAD perlu dikombinasikan dengan metodologi lain yang fokus pada kualitas produk akhir.

6. **Agile Development (XP)**  
   **Kelebihan:**
   - Sangat fleksibel dan memungkinkan iterasi cepat dengan masukan pengguna yang sering. Setiap fitur dapat dikembangkan dan diuji dalam siklus pendek, sehingga feedback dapat diterima dan diterapkan segera.
   - Cocok untuk proyek yang membutuhkan penyesuaian berkelanjutan dan adaptasi terhadap perubahan kebutuhan. Agile sangat efektif untuk pengembangan AI karena memungkinkan perbaikan algoritma secara bertahap.
   - Menekankan kolaborasi tim yang intensif dan komunikasi, yang membantu dalam memadukan pengembangan AI dengan antarmuka pengguna secara efisien.

   **Kekurangan:**
   - Membutuhkan keterlibatan pengguna secara aktif dan konstan, yang mungkin sulit jika tidak ada akses berkelanjutan terhadap pengguna.
   - Dokumentasi bisa kurang mendetail karena fokus pada pengiriman cepat dalam tiap iterasi, yang dapat menjadi kendala jika diperlukan dokumentasi lengkap di kemudian hari.

   **Relevansi untuk projek ini:**
   Agile sangat cocok untuk proyek ini karena fleksibilitas dan pendekatan iteratifnya. Dalam konteks projek ini, Agile memungkinkan perbaikan terus-menerus pada model AI deteksi emosi dan antarmuka pengguna berdasarkan feedback siswa dan guru, sehingga pada Agile, projek dapat beradaptasi terhadap kebutuhan dan kendala yang mungkin muncul selama pengembangan.

### Rekomendasi Analisis Akhir

**Agile Development (XP)** adalah pilihan terbaik untuk projek kami. Agile memungkinkan kami untuk fokus pada perbaikan kualitas secara berkelanjutan, menerima feedback pengguna secara cepat, dan mengimplementasikan penyesuaian dengan segera, sehingga dengan menggunakan Agile, kami dapat memastikan aplikasi berkembang sesuai kebutuhan, seperti memperbaiki akurasi AI dalam mengenali emosi siswa dan menyempurnakan antarmuka pengguna.

### Penerapan Agile pada projek ini mencakup:
- **Sprint AI** untuk pengembangan dan penyempurnaan model deteksi emosi, dengan tujuan meningkatkan akurasi berdasarkan masukan pengguna.
- **Sprint Antarmuka** untuk memperbaiki UX/UI aplikasi, memastikan antarmuka mudah dipahami dan memberikan pengalaman yang intuitif bagi siswa dan guru.
- **Feedback Rutin** dari guru dan siswa setelah setiap iterasi, sehingga pengembangan aplikasi dapat disesuaikan sesuai umpan balik langsung dari pengguna.

Sehingga dengan **Agile**, projek ini dapat berkembang menjadi aplikasi yang adaptif dan efektif, memberikan pengalaman pengguna yang lebih baik dan mendukung keberhasilan pembelajaran jarak jauh secara optimal.

</p>
