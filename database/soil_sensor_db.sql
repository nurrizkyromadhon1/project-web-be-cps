-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 15 Okt 2024 pada 10.03
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `soil_sensor_db`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `soil_data`
--

CREATE TABLE `soil_data` (
  `id` int(11) NOT NULL,
  `temperature` float DEFAULT NULL,
  `moisture` float DEFAULT NULL,
  `pH` float DEFAULT NULL,
  `conductivity` float DEFAULT NULL,
  `nitrogen` float DEFAULT NULL,
  `phosphorus` float DEFAULT NULL,
  `potassium` float DEFAULT NULL,
  `timestamp` datetime DEFAULT current_timestamp(),
  `tanaman` varchar(50) DEFAULT NULL,
  `tanaman_no` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `soil_data`
--

INSERT INTO `soil_data` (`id`, `temperature`, `moisture`, `pH`, `conductivity`, `nitrogen`, `phosphorus`, `potassium`, `timestamp`, `tanaman`, `tanaman_no`) VALUES
(1, 25.5, 45, 6.8, 1.2, 3.4, 2.5, 1.8, '2024-10-13 18:43:50', 'cabai', 1),
(2, 1, 2, 3, 4, 5, 6, 7, '2024-10-14 20:06:53', 'cabai', 2),
(3, 25.5, 50, 9.8, 4.2, 3.4, 2.5, 4.8, '2024-10-15 20:08:44', 'kemangi', 1),
(4, 25.5, 45, 6.8, 1.2, 3.4, 2.5, 1.8, '2024-10-16 00:00:00', 'kemangi', 2),
(5, 25.5, 45, 6.8, 1.2, 3.4, 2.5, 1.8, '2024-10-17 00:00:00', 'kemangi', 1),
(6, 25.5, 45, 6.8, 1.2, 3.4, 2.5, 1.8, '2024-10-18 13:04:24', 'cabai', 1);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `soil_data`
--
ALTER TABLE `soil_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `soil_data`
--
ALTER TABLE `soil_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
