# EduDOExam - Aplikasi Pemantau Keterlibatan dan Fokus Siswa Berbasis AI untuk Pembelajaran Jarak Jauh

## 1. Latar Belakang:
<p align="justify">
Perkembangan teknologi informasi dan komunikasi telah membawa perubahan signifikan dalam bidang pendidikan. Salah satu inovasi penting adalah penerapan ujian online yang memungkinkan siswa untuk mengakses soal dari mana saja dan kapan saja. Meskipun fleksibel dan efisien, guru sering kesulitan memantau keterlibatan emosional dan fokus siswa, terutama dalam pembelajaran jarak jauh. Tanpa pemahaman menyeluruh tentang kondisi mental siswa, interaksi menjadi kurang efektif, dan proses pembelajaran pun tidak maksimal. EduDOExam hadir sebagai solusi untuk meningkatkan kinerja pembelajaran siswa dengan memanfaatkan teknologi AI. Aplikasi ini memungkinkan pemantauan kondisi emosional siswa selama ujian, memberikan informasi penting yang dapat membantu guru memahami dan merespons kebutuhan siswa dengan lebih baik.

## 2. Ruang Lingkup dan Batasan:
### - Ruang Lingkup:
<p align="justify">
EduDOExam adalah aplikasi mobile berbasis AI yang dirancang untuk mendukung pembelajaran jarak jauh di tingkat SMA di Indonesia. Fokus pada tingkat SMA ini didasarkan pada implementasi sistem pembelajaran jarak jauh yang lebih umum diterapkan pada jenjang ini. Aplikasi ini hanya dapat diakses melalui perangkat smartphone, yang lebih terjangkau dan umum dimiliki oleh siswa SMA dibandingkan laptop. Setiap sesi ujian dibatasi untuk maksimal 40 siswa per kelas untuk menghindari masalah teknis seperti server overload dan konektivitas yang tidak stabil.

### - Batasan:
<p align="justify">
Aplikasi ini terbatas pada penggunaan smartphone dan tidak dapat diakses melalui perangkat lain seperti laptop. Fitur deteksi emosi hanya dapat berfungsi jika kamera perangkat aktif. Jika izin akses kamera tidak diberikan, fitur ini tidak akan tersedia bagi siswa. Data kinerja siswa, termasuk grafik performa, disimpan di cloud yang memerlukan biaya penyimpanan. Kenaikan jumlah pengguna dapat meningkatkan biaya operasional, sehingga diperlukan opsi pembiayaan tambahan atau model premium untuk mendukung penyimpanan yang lebih besar.

## 3. Fitur yang Didapat oleh Siswa dan Guru:
### - Fitur untuk Siswa:
- **Login/Logout**: Siswa harus mendaftar dan login untuk mengakses aplikasi.
- **Mengerjakan Soal**: Siswa dapat mengakses soal yang telah disiapkan oleh guru dan mengerjakannya di dalam aplikasi.
- **Melihat Peraturan Pengerjaan Soal**: Siswa memiliki akses untuk melihat instruksi atau aturan terkait pengerjaan soal.
- **Memilih Mata Pelajaran**: Siswa dapat memilih mata pelajaran yang ingin diuji, dan sistem akan menampilkan soal sesuai pilihan mereka.
- **Mengakses Kamera**: Siswa perlu mengaktifkan kamera untuk memungkinkan sistem memantau ekspresi wajah mereka sebagai bagian dari analisis emosi selama pengerjaan soal.
- **Mendapatkan Rekomendasi Soal Selanjutnya**: Aplikasi memberikan rekomendasi soal selanjutnya berdasarkan kondisi emosi siswa, membantu menjaga keterlibatan siswa.
- **Melihat Performa Pengerjaan dalam Bentuk Diagram**: Setelah selesai mengerjakan soal, siswa dapat melihat performa mereka dalam bentuk diagram visual.
- **Notifikasi Reminder untuk Mengerjakan Ulangan**: Sistem mengirimkan notifikasi sebagai pengingat bagi siswa untuk mengerjakan ulangan yang dijadwalkan.

### - Fitur untuk Guru:
- **Login dan Daftar**: Guru juga diwajibkan mendaftar dan login untuk mengelola data dan akses ke sistem.
- **Akses Data Kinerja Setiap Siswa**: Guru dapat melihat, merekap, dan menyimpan data kinerja siswa ke penyimpanan lokal untuk analisis lebih lanjut.
- **Membuat Sesi Ulangan**: Guru memiliki kendali penuh untuk mengelola sesi ulangan, termasuk menambah atau menghapus sesi, mengatur waktu mulai dan akhir ujian, serta menentukan durasi pengerjaan soal.

## 4. Risiko dan Isu Terkait Proyek:
### - Risiko Teknis:
- **Server Overload**: Dengan batasan maksimum 40 siswa per sesi, ada risiko server overload jika banyak siswa mengakses aplikasi secara bersamaan, yang dapat menyebabkan aplikasi menjadi lambat atau bahkan crash.
- **Akurasi Deteksi Emosi**: Model AI yang digunakan mungkin memiliki keterbatasan dalam mengenali emosi di berbagai kondisi pencahayaan dan ekspresi wajah, yang dapat mempengaruhi keakuratan hasil deteksi.
- **Koneksi Internet yang Tidak Stabil**: Karena aplikasi bergantung pada koneksi internet, jaringan yang lambat atau tidak stabil dapat menghambat proses deteksi emosi dan pelaporan performa siswa.

### - Risiko Keamanan dan Privasi:
- **Kerahasiaan Data Siswa**: EduDOExam menyimpan data pribadi dan performa siswa, termasuk data visual emosi. Penting untuk memastikan bahwa data ini terlindungi dari akses tidak sah sesuai peraturan perlindungan data.
- **Biaya Penyimpanan Cloud**: Penyimpanan data kinerja siswa di cloud dalam bentuk grafik performa dapat menambah biaya operasional. Kenaikan penggunaan aplikasi mungkin memerlukan model pembiayaan tambahan atau opsi premium.

### - Risiko Pengguna:
- **Keterbatasan Perangkat Siswa**: Tidak semua siswa memiliki smartphone dengan spesifikasi memadai atau koneksi internet stabil, yang dapat membatasi akses mereka terhadap aplikasi ini.
- **Ketergantungan pada Teknologi**: Guru dan siswa perlu memiliki pemahaman dasar tentang penggunaan teknologi, terutama terkait izin akses kamera dan fitur digital lainnya. Keterbatasan literasi digital dapat menjadi hambatan.

### - Isu Potensial:
- **Kapasitas Penyimpanan dan Biaya Operasional**: Penyimpanan data emosi dalam bentuk grafik di cloud berpotensi meningkatkan biaya. Dalam jangka panjang, perlu ada strategi pembiayaan untuk menjaga keberlanjutan aplikasi.
- **Variasi Literasi Digital**: Tingkat pemahaman teknologi di kalangan siswa dan guru mungkin bervariasi. Hal ini bisa menjadi kendala bagi pengguna yang kurang familiar dengan aplikasi atau perangkat digital.
- **Ketergantungan pada Izin Kamera**: Fitur utama aplikasi yang bergantung pada akses kamera akan menjadi tidak efektif jika siswa menolak atau lupa memberikan izin kamera.
