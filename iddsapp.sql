-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for lddsdb2023
CREATE DATABASE IF NOT EXISTS `lddsdb2023` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `lddsdb2023`;

-- Dumping structure for table lddsdb2023.administrator
CREATE TABLE IF NOT EXISTS `administrator` (
  `id` int NOT NULL AUTO_INCREMENT,
  `role_Id` int NOT NULL,
  `name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `surname` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `username` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `phone` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `gender` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `city` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_73A716F4387060E` (`role_Id`),
  CONSTRAINT `FK_73A716F4387060E` FOREIGN KEY (`role_Id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- Dumping data for table lddsdb2023.administrator: ~8 rows (approximately)
INSERT IGNORE INTO `administrator` (`id`, `role_Id`, `name`, `surname`, `username`, `password`, `email`, `phone`, `gender`, `city`, `address`, `created_at`, `updated_at`) VALUES
	(1, 1, 'Anita', 'Admin', 'Ewc100', '$2y$12$zlCTUWaI0t6orJmjypjwCOLmeQ3g.lp0BURapdNKXTwXcpI59d6/a', 'superadmin@wilson.com', '0776452244', 'Male', 'Bulawayo', '12 Cliffe Akedia', '2023-11-13 21:18:14', NULL),
	(2, 2, 'Innocent', 'Jack', 'Ewc101', '0392dd13ae49e5a8fcf91becf6fe060d0b36d7ee', 'inn@wilson.com', '0776452244', 'Male', 'Harare', '12 Cliffe Akedia', '2023-11-13 21:18:14', NULL),
	(3, 1, 'Anita', 'Wilson', 'Super', '0392dd13ae49e5a8fcf91becf6fe060d0b36d7ee', 'admin@wilson.com', '0776452244', 'Female', 'Harare', '12 Cliffe Akedia', '2023-11-18 14:14:35', NULL),
	(4, 2, 'Aubrey', 'Gahadzikwa', NULL, '0392dd13ae49e5a8fcf91becf6fe060d0b36d7ee', 'aagaha@gmail.com', '0776452244', 'Male', 'Harare', '12 Cliffe Akedia', '2023-11-19 13:20:23', NULL),
	(5, 2, 'Abigal', 'Mandiomera', NULL, '0392dd13ae49e5a8fcf91becf6fe060d0b36d7ee', 'abigalmandiomera@gmail.com', '0774914150', 'Female', 'Harare', '4474 Hatcliffe Extension', '2023-11-20 20:17:39', NULL),
	(6, 2, 'Andile', 'Tauzeni', NULL, 'e9c7dc117f43a480fbb8304d9f535fab186fced5', 'atauzeni@gmail.com', '0774914158', 'Male', 'Harare', '4474 Hatcliffe Extension', '2023-11-26 12:16:34', NULL),
	(7, 1, 'Keryleen', 'Tauzeni', NULL, '0392dd13ae49e5a8fcf91becf6fe060d0b36d7ee', 'kerlyeentauzeni@gmail.com', '0774914155', 'Female', 'Harare', '6731 Sirdic Street Hatcliffe', '2023-11-26 13:34:28', NULL),
	(9, 2, 'Dennishia', 'MaringaH', NULL, '0392dd13ae49e5a8fcf91becf6fe060d0b36d7ee', 'dmaringa@gmail.com', '0777998657', 'Female', 'Harare', '4474 Hatcliffe Extension', '2023-11-28 20:05:30', NULL);

-- Dumping structure for table lddsdb2023.audit
CREATE TABLE IF NOT EXISTS `audit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `administrator_id` int NOT NULL,
  `entity` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `oldvalue` longtext COLLATE utf8mb3_unicode_ci,
  `newvalue` longtext COLLATE utf8mb3_unicode_ci,
  `action` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_32451E6C4B09E92C` (`administrator_id`),
  CONSTRAINT `FK_32451E6C4B09E92C` FOREIGN KEY (`administrator_id`) REFERENCES `administrator` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- Dumping data for table lddsdb2023.audit: ~2 rows (approximately)
INSERT IGNORE INTO `audit` (`id`, `administrator_id`, `entity`, `oldvalue`, `newvalue`, `action`, `created_at`, `updated_at`) VALUES
	(1, 7, 'Role', 'N/A', '{\'name\': \'Super Admin\'}', 'CREATE ROLE', '2023-11-28 20:40:57', NULL),
	(2, 7, 'Role', '{\'name\': \'Super Admin\'}', '{\'name\': \'DELETED\'}', 'DELETE ROLE', '2023-11-28 20:49:56', NULL),
	(3, 7, 'Desease', '{\'name\': \'BLUE SILL\', \'systoms\': \'BLUE SILL\', \'imageurl\': \'logo.png\'}', '{\'name\': \'DELETED\'}', 'DELETE DESEASE', '2023-11-28 21:10:02', NULL);

-- Dumping structure for table lddsdb2023.desease
CREATE TABLE IF NOT EXISTS `desease` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `systoms` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `imageurl` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- Dumping data for table lddsdb2023.desease: ~7 rows (approximately)
INSERT IGNORE INTO `desease` (`id`, `name`, `systoms`, `imageurl`, `created_at`, `updated_at`) VALUES
	(1, 'NORTHEN LEAF BLIGHT', 'Symptoms appear on the leaves in the form of longitudinal spindle-shaped spots that are small in size at first, greenish-gray in color, then they grow with the progression of the infection and may reach in an area of more than (20 cm in length and 3 cm in width). It turns light brown. The spots are seen on the lower leaves first about 40 days after planting and then spread on the upper leaves with time. In severe infections, the spots permeate most of the surface area of the leaves and fuse with each other, which leads to the drying of the leaves completely and thus the death of the plants', 'Corn_Blight (16).jpg', '2023-11-15 13:19:18', '2023-11-16 10:08:40'),
	(2, 'GRAY LEAF SPOT', 'It is the production of a phytotoxin called Cercospora zeae-maydis one of the reasons for the pathogenic success of inactive cercosporin.All members of the genus Cercospora produce this light-activated toxin during infection. In the absence of light, cercosporin is inactive, but when light is present, the toxin is converted to its excited triplet state.', 'Corn_Gray_Spot (29).jpg', '2023-11-15 13:23:19', NULL),
	(3, 'COMMON RUST', 'Symptoms of the disease appear in the form of fine speckling on both sides of the leaves which slowly develop into small dark and slightly prominent spots. These mainly elongated spots later turn into golden brown pustules irregularly spread in spots on the upper and lower sides. Its color can change to black with the growth of the plant. In contrast to other rust diseases such as: stems, leaves, sheaths and scales. However, the stems grow weak and soft and are more prone to falling. Younger leaf tissues are more susceptible to fungal infection than fully developed leaves. Infected plants during the early stages can show yellowing due to the lack of chlorophyll in the leaves and die. This leads to losses if the upper leaves are affected.', 'Corn_Common_Rust (2).jpg', '2023-11-15 13:24:24', NULL),
	(4, 'MAIZE STREAK VIRUS', 'Transmitted by a leafhopper insect, this viral disease causes chlorotic streaking or yellowing of the leaves. Infected plants may also display stunted growth and reduced yields.', 'logo.png', '2023-11-15 13:28:15', NULL),
	(7, 'SOUTHERN BLIGHT LEAF', 'leaf', 'logo.png', '2023-11-18 22:26:26', NULL),
	(8, 'EAST BLIGHT LEAF33', 'Huya', 'logo.png', '2023-11-26 16:29:37', NULL);

-- Dumping structure for table lddsdb2023.deseaselog
CREATE TABLE IF NOT EXISTS `deseaselog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `administrator_id` int NOT NULL,
  `desease_Id` int NOT NULL,
  `ipaddress` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `geolocationap` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `country` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `city` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `province` varchar(255) DEFAULT NULL,
  `district` varchar(255) DEFAULT NULL,
  `useaccountname` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `IDX_705C757D4B09E92A` (`administrator_id`) USING BTREE,
  KEY `IDX_705C758D4B09E82A` (`desease_Id`) USING BTREE,
  CONSTRAINT `FK_705C757D4B09E92A` FOREIGN KEY (`administrator_id`) REFERENCES `administrator` (`id`),
  CONSTRAINT `FK_705C758D4B09E82A` FOREIGN KEY (`desease_Id`) REFERENCES `desease` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table lddsdb2023.deseaselog: ~11 rows (approximately)
INSERT IGNORE INTO `deseaselog` (`id`, `administrator_id`, `desease_Id`, `ipaddress`, `geolocationap`, `country`, `city`, `province`, `district`, `useaccountname`, `created_at`, `updated_at`) VALUES
	(1, 3, 3, '1::', 'N/A', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Anita Wilson', '2023-11-28 15:08:28', NULL),
	(2, 3, 2, '1::', 'N/A', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Anita Wilson', '2023-11-28 19:37:28', NULL),
	(3, 2, 3, '1::', 'N/A', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Innocent Jack', '2023-11-28 21:31:01', NULL),
	(4, 2, 2, '1::', 'N/A', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Innocent Jack', '2023-11-28 21:31:16', NULL),
	(5, 2, 1, '1::', 'N/A', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Innocent Jack', '2023-11-28 21:31:56', NULL),
	(6, 4, 2, '1::', 'N/A', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Aubrey Gahadzikwa', '2023-11-28 21:38:56', NULL),
	(7, 6, 2, '1::', 'N/A', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Andile Tauzeni', '2023-11-29 06:30:24', NULL),
	(8, 6, 1, '1::', 'N/A', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Andile Tauzeni', '2023-11-29 06:35:51', NULL),
	(9, 6, 3, '1::', 'N/A', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Andile Tauzeni', '2023-11-29 06:36:17', NULL),
	(10, 3, 2, '41.175.87.179', 'N/A', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Anita Wilson', '2023-11-29 09:16:48', NULL),
	(11, 3, 2, '41.175.87.179', '{\'latitude\': -17.826669692993164, \'longitude\': 31.053329467773438}', 'Zimbabwe', 'Harare', 'Harare', 'Harare', 'Anita Wilson', '2023-11-29 09:24:28', NULL);

-- Dumping structure for table lddsdb2023.provinces
CREATE TABLE IF NOT EXISTS `provinces` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- Dumping data for table lddsdb2023.provinces: ~0 rows (approximately)

-- Dumping structure for table lddsdb2023.recommendation
CREATE TABLE IF NOT EXISTS `recommendation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `desease_Id` int NOT NULL,
  `recommendationmessage` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_7832B3F7AB8584F7` (`desease_Id`),
  CONSTRAINT `FK_7832B3F7AB8584F7` FOREIGN KEY (`desease_Id`) REFERENCES `desease` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- Dumping data for table lddsdb2023.recommendation: ~5 rows (approximately)
INSERT IGNORE INTO `recommendation` (`id`, `desease_Id`, `recommendationmessage`, `created_at`, `updated_at`) VALUES
	(2, 1, 'Early planting before mid-June so that plants in the vegetative growth stage are not exposed to the appropriate conditions for the spread of the disease.When the disease spreads, the affected leaves are collected and burned. In severe infestations, we use appropriate fungicides such as (propiconazole - azoxystrobin - pyraclostrobin). You have to plant varieties that are resistant or tolerant to the disease.Ensure the abundance of balanced nutrients, avoid excessive nitrogen fertilization, and regularly remove weeds from the field and surrounding area.Rotate the plantings with soybeans, beans or sunflowers to avoid the widespread spread of the disease, and use a deep plow to bury plant debris and reduce the amount of pollen in the soil.', '2023-11-16 07:51:55', '2023-11-16 10:56:20'),
	(3, 3, 'Cultivation of disease-resistant varieties.And plant early to avoid optimal conditions for infection.You should use varieties that mature quickly and in a shorter period.\r\nMonitor your crop regularly for signs of disease, and intensify monitoring during cloudy weather.\r\nYou must also ensure a balanced fertilization with nitrogen application. 6.Moderation in nitrogen fertilization because * its increase leads to an increase in the incidence of disease, with interest in potassium fertilization.\r\nCrop rotation with non-susceptible crops. 8.It was possible to treat this disease by using systemic fungicides such as *Saprol Ondar when the infection appeared. 9.Reducing moisture around plants by moderating irrigation and increasing planting distances\r\n', '2023-11-16 07:55:23', '2023-11-16 09:55:23'),
	(4, 2, 'fgggggggggggggggggggggggggggggg', '2023-11-19 12:29:46', NULL),
	(5, 4, 'sjjsjjsjsjs  sjjjhddhhddjdh  xxjxxj kkzkzkzk lzlzkzkzk   xxhxhxhxhx ixhhxhxhx nxjxjxjxjxj xhxhxhx  kjxjxjjkcx', '2023-11-19 12:33:07', NULL),
	(6, 7, 'xxxx fffff', '2023-11-19 12:33:41', NULL),
	(7, 8, 'Amania', '2023-11-26 17:18:08', NULL);

-- Dumping structure for table lddsdb2023.role
CREATE TABLE IF NOT EXISTS `role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UNIQ_B63E2EC75E237E06` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- Dumping data for table lddsdb2023.role: ~2 rows (approximately)
INSERT IGNORE INTO `role` (`id`, `name`, `created_at`, `updated_at`) VALUES
	(1, 'Administrator', '2023-11-13 21:16:45', NULL),
	(2, 'User', '2023-11-13 21:16:45', NULL);

-- Dumping structure for table lddsdb2023.systemlog
CREATE TABLE IF NOT EXISTS `systemlog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `administrator_id` int NOT NULL,
  `timein` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `ipaddress` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `geolocationap` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `country` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `city` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `useaccountname` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `timeout` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `status` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci DEFAULT 'PENDING',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `IDX_705C757D4B09E92C` (`administrator_id`),
  CONSTRAINT `FK_705C757D4B09E92C` FOREIGN KEY (`administrator_id`) REFERENCES `administrator` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

-- Dumping data for table lddsdb2023.systemlog: ~24 rows (approximately)
INSERT IGNORE INTO `systemlog` (`id`, `administrator_id`, `timein`, `ipaddress`, `geolocationap`, `country`, `city`, `useaccountname`, `timeout`, `status`, `created_at`, `updated_at`) VALUES
	(1, 3, '2023-11-28 16:28:13', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Anita Wilson', '2023-11-28 16:46:09', 'Logged out', '2023-11-28 14:28:13', NULL),
	(2, 3, '2023-11-28 16:46:40', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Anita Wilson', '2023-11-28 16:46:56', 'Logged out', '2023-11-28 14:46:40', NULL),
	(3, 5, '2023-11-28 16:47:14', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Abigal Mandiomera', '2023-11-28 16:47:29', 'Logged out', '2023-11-28 14:47:14', NULL),
	(4, 5, '2023-11-28 16:48:30', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Abigal Mandiomera', '2023-11-28 16:48:36', 'Logged out', '2023-11-28 14:48:30', NULL),
	(5, 3, '2023-11-28 16:48:40', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Anita Wilson', '2023-11-28 17:42:45', 'Logged out', '2023-11-28 14:48:40', NULL),
	(6, 6, '2023-11-28 17:43:20', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Andile Tauzeni', '2023-11-28 17:43:39', 'Logged out', '2023-11-28 15:43:20', NULL),
	(7, 3, '2023-11-28 21:36:40', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Anita Wilson', '2023-11-28 21:44:39', 'Logged out', '2023-11-28 19:36:40', NULL),
	(8, 6, '2023-11-28 21:44:47', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Andile Tauzeni', '2023-11-28 21:45:49', 'Logged out', '2023-11-28 19:44:47', NULL),
	(9, 7, '2023-11-28 21:46:32', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Keryleen Tauzeni', '2023-11-28 23:17:00', 'Logged out', '2023-11-28 19:46:32', NULL),
	(10, 6, '2023-11-28 23:21:14', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Andile Tauzeni', '2023-11-28 23:21:43', 'Logged out', '2023-11-28 21:21:14', NULL),
	(11, 3, '2023-11-28 23:21:51', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Anita Wilson', '2023-11-28 23:23:38', 'Logged out', '2023-11-28 21:21:51', NULL),
	(12, 6, '2023-11-28 23:23:45', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Andile Tauzeni', '2023-11-28 23:24:15', 'Logged out', '2023-11-28 21:23:45', NULL),
	(13, 2, '2023-11-28 23:24:22', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Innocent Jack', '2023-11-28 23:24:54', 'Logged out', '2023-11-28 21:24:22', NULL),
	(14, 3, '2023-11-28 23:25:03', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Anita Wilson', '2023-11-28 23:30:32', 'Logged out', '2023-11-28 21:25:03', NULL),
	(15, 2, '2023-11-28 23:30:39', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Innocent Jack', '2023-11-28 23:36:51', 'Logged out', '2023-11-28 21:30:39', NULL),
	(16, 3, '2023-11-28 23:36:59', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Anita Wilson', '2023-11-28 23:38:20', 'Logged out', '2023-11-28 21:36:59', NULL),
	(17, 4, '2023-11-28 23:38:32', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Aubrey Gahadzikwa', '2023-11-28 23:40:07', 'Logged out', '2023-11-28 21:38:32', NULL),
	(18, 5, '2023-11-28 23:40:17', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Abigal Mandiomera', '2023-11-28 23:41:47', 'Logged out', '2023-11-28 21:40:17', NULL),
	(19, 5, '2023-11-29 05:48:56', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Abigal Mandiomera', '2023-11-29 05:49:05', 'Logged out', '2023-11-29 03:48:56', NULL),
	(20, 3, '2023-11-29 05:49:20', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Anita Wilson', '2023-11-29 06:54:13', 'Logged out', '2023-11-29 03:49:20', NULL),
	(21, 5, '2023-11-29 06:54:19', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Abigal Mandiomera', '2023-11-29 08:29:28', 'Logged out', '2023-11-29 04:54:19', NULL),
	(22, 6, '2023-11-29 08:29:39', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Andile Tauzeni', '2023-11-29 08:59:40', 'Logged out', '2023-11-29 06:29:39', NULL),
	(23, 6, '2023-11-29 08:31:19', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Andile Tauzeni', 'PENDING', 'PENDING', '2023-11-29 06:31:19', NULL),
	(24, 3, '2023-11-29 08:59:46', 'N/A', 'N/A', 'Zimbabwe', 'Harare', 'Anita Wilson', 'PENDING', 'PENDING', '2023-11-29 06:59:46', NULL);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
