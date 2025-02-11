-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: remedydb
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `areas`
--

DROP TABLE IF EXISTS `areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `areas` (
  `Area ID` varchar(255) NOT NULL,
  `Location` varchar(255) NOT NULL,
  `GPS` varchar(255) NOT NULL,
  PRIMARY KEY (`Area ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `areas`
--

LOCK TABLES `areas` WRITE;
/*!40000 ALTER TABLE `areas` DISABLE KEYS */;
INSERT INTO `areas` VALUES ('A001','Area1','hyd'),('A002','Area2','hyd'),('A003','Area3','hyd'),('A004','Area4','hyd');
/*!40000 ALTER TABLE `areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assessment`
--

DROP TABLE IF EXISTS `assessment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assessment` (
  `Assessment ID` int NOT NULL AUTO_INCREMENT,
  `User ID` varchar(255) DEFAULT NULL,
  `Pile ID` varchar(255) DEFAULT NULL,
  `Task Date` date NOT NULL,
  `Allotted Date` date NOT NULL,
  `Allotted By` varchar(255) DEFAULT NULL,
  `Date Completed` date DEFAULT NULL,
  `Assessment Status` varchar(255) NOT NULL,
  `Assessment Case` varchar(255) NOT NULL,
  `Picture Name` varchar(255) NOT NULL,
  `Picture Location` varchar(255) NOT NULL,
  PRIMARY KEY (`Assessment ID`),
  KEY `User ID` (`User ID`),
  KEY `Pile ID` (`Pile ID`),
  KEY `Allotted By` (`Allotted By`),
  CONSTRAINT `assessment_ibfk_1` FOREIGN KEY (`User ID`) REFERENCES `users` (`User ID`),
  CONSTRAINT `assessment_ibfk_2` FOREIGN KEY (`Pile ID`) REFERENCES `piles` (`Pile ID`),
  CONSTRAINT `assessment_ibfk_3` FOREIGN KEY (`Allotted By`) REFERENCES `users` (`User ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assessment`
--

LOCK TABLES `assessment` WRITE;
/*!40000 ALTER TABLE `assessment` DISABLE KEYS */;
INSERT INTO `assessment` VALUES (10,'U001','p','2025-01-08','2025-01-08','U001','2025-01-08','Final','Corrosion3','',''),(14,'U002','p','2025-01-09','2025-01-10','U001','2025-01-10','Incomplete','Corrosion2','','');
/*!40000 ALTER TABLE `assessment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assessmentupdate`
--

DROP TABLE IF EXISTS `assessmentupdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assessmentupdate` (
  `assessment_id` int NOT NULL,
  `task_date` date NOT NULL,
  `updated_by` varchar(255) NOT NULL,
  `assessment_status` varchar(255) NOT NULL,
  `corrosion_status` varchar(255) NOT NULL,
  `pic_address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`assessment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assessmentupdate`
--

LOCK TABLES `assessmentupdate` WRITE;
/*!40000 ALTER TABLE `assessmentupdate` DISABLE KEYS */;
/*!40000 ALTER TABLE `assessmentupdate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `Comment ID` int NOT NULL AUTO_INCREMENT,
  `Comment Type` varchar(255) DEFAULT NULL,
  `Related Comment ID` varchar(255) DEFAULT NULL,
  `Pile ID` varchar(255) DEFAULT NULL,
  `User ID` varchar(255) DEFAULT NULL,
  `Usage ID` varchar(255) DEFAULT NULL,
  `Date Posted` date DEFAULT NULL,
  `Comment Text` varchar(255) NOT NULL,
  `Comment Date` date DEFAULT NULL,
  `Commented By` varchar(255) DEFAULT NULL,
  `Status` varchar(255) NOT NULL,
  PRIMARY KEY (`Comment ID`),
  KEY `Pile ID` (`Pile ID`),
  KEY `User ID` (`User ID`),
  KEY `Commented By` (`Commented By`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`Pile ID`) REFERENCES `piles` (`Pile ID`),
  CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`User ID`) REFERENCES `users` (`User ID`),
  CONSTRAINT `comments_ibfk_3` FOREIGN KEY (`Commented By`) REFERENCES `users` (`User ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `Cust ID` varchar(255) NOT NULL,
  `Customer Name` varchar(255) DEFAULT NULL,
  `Customer Address` varchar(255) DEFAULT NULL,
  `Contact person` varchar(255) DEFAULT NULL,
  `Customer Website` varchar(255) DEFAULT NULL,
  `Phone No` varchar(255) DEFAULT NULL,
  `Country` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Cust ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('C011','NARESH JANGA','hyd','nm','https://indisolar.com/','1234567899','CN');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `Item ID` varchar(255) NOT NULL,
  `Item Type` varchar(255) NOT NULL,
  `Item UOM` varchar(255) NOT NULL,
  `Item Desc` varchar(255) NOT NULL,
  `Item Avl Qty` varchar(255) NOT NULL,
  `Item ROR` varchar(255) NOT NULL,
  `Item Value` varchar(255) DEFAULT NULL,
  `Item Rate` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Item ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('I001','1112','a','12','a','2',NULL,NULL);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invtrans`
--

DROP TABLE IF EXISTS `invtrans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invtrans` (
  `Item ID` varchar(255) NOT NULL,
  `Trans Qty` varchar(255) NOT NULL,
  `Trans Type` varchar(255) NOT NULL,
  `Trans Date` date NOT NULL,
  `User ID` varchar(255) DEFAULT NULL,
  `Usage` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invtrans`
--

LOCK TABLES `invtrans` WRITE;
/*!40000 ALTER TABLE `invtrans` DISABLE KEYS */;
INSERT INTO `invtrans` VALUES ('1','1','1','2025-01-08','1','1');
/*!40000 ALTER TABLE `invtrans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loginusers`
--

DROP TABLE IF EXISTS `loginusers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loginusers` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loginusers`
--

LOCK TABLES `loginusers` WRITE;
/*!40000 ALTER TABLE `loginusers` DISABLE KEYS */;
INSERT INTO `loginusers` VALUES (1,'naresh','nareshjanga966@gmail.com','123'),(2,'hi','hi@123','123');
/*!40000 ALTER TABLE `loginusers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `piles`
--

DROP TABLE IF EXISTS `piles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `piles` (
  `Pile ID` varchar(255) NOT NULL DEFAULT 'P',
  `Table ID` varchar(255) DEFAULT NULL,
  `Row ID` varchar(255) DEFAULT NULL,
  `Area ID` varchar(255) DEFAULT NULL,
  `Location Description` varchar(255) DEFAULT NULL,
  `GPS Location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Pile ID`),
  KEY `Table ID` (`Table ID`),
  KEY `Row ID` (`Row ID`),
  KEY `Area ID` (`Area ID`),
  CONSTRAINT `piles_ibfk_1` FOREIGN KEY (`Table ID`) REFERENCES `tables` (`Table ID`),
  CONSTRAINT `piles_ibfk_2` FOREIGN KEY (`Row ID`) REFERENCES `rows` (`Row ID`),
  CONSTRAINT `piles_ibfk_3` FOREIGN KEY (`Area ID`) REFERENCES `areas` (`Area ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `piles`
--

LOCK TABLES `piles` WRITE;
/*!40000 ALTER TABLE `piles` DISABLE KEYS */;
INSERT INTO `piles` VALUES ('P','T001','R001','A001','122w','');
/*!40000 ALTER TABLE `piles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remedy`
--

DROP TABLE IF EXISTS `remedy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `remedy` (
  `Remedy ID` int NOT NULL AUTO_INCREMENT,
  `User ID` varchar(255) DEFAULT NULL,
  `Pile ID` varchar(255) DEFAULT NULL,
  `Task Date` date NOT NULL,
  `Assessed Case` varchar(255) NOT NULL,
  `Allotted Date` date NOT NULL,
  `Allotted By` varchar(255) DEFAULT NULL,
  `Date Completed` date DEFAULT NULL,
  `Remedy Status` varchar(255) NOT NULL,
  `Remedy Text` varchar(255) DEFAULT NULL,
  `Picture Name` varchar(255) NOT NULL,
  `Picture Location` varchar(255) NOT NULL,
  PRIMARY KEY (`Remedy ID`),
  KEY `User ID` (`User ID`),
  KEY `Pile ID` (`Pile ID`),
  KEY `Allotted By` (`Allotted By`),
  CONSTRAINT `remedy_ibfk_1` FOREIGN KEY (`User ID`) REFERENCES `users` (`User ID`),
  CONSTRAINT `remedy_ibfk_2` FOREIGN KEY (`Pile ID`) REFERENCES `piles` (`Pile ID`),
  CONSTRAINT `remedy_ibfk_3` FOREIGN KEY (`Allotted By`) REFERENCES `users` (`User ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remedy`
--

LOCK TABLES `remedy` WRITE;
/*!40000 ALTER TABLE `remedy` DISABLE KEYS */;
INSERT INTO `remedy` VALUES (9,NULL,NULL,'2025-01-08','Corrosion1','2025-01-08',NULL,NULL,'Under review',NULL,'2025-01-08','2025-01-08');
/*!40000 ALTER TABLE `remedy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remedyupdate`
--

DROP TABLE IF EXISTS `remedyupdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `remedyupdate` (
  `remedy_id` int NOT NULL,
  `task_date` date NOT NULL,
  `updated_by` varchar(255) NOT NULL,
  `remedy_status` varchar(255) NOT NULL,
  `pic_address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`remedy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remedyupdate`
--

LOCK TABLES `remedyupdate` WRITE;
/*!40000 ALTER TABLE `remedyupdate` DISABLE KEYS */;
/*!40000 ALTER TABLE `remedyupdate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rows`
--

DROP TABLE IF EXISTS `rows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rows` (
  `Row ID` varchar(255) NOT NULL,
  `Row Name` varchar(255) NOT NULL,
  `Area ID` varchar(255) DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `GPS` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Row ID`),
  KEY `rows_ibfk_1` (`Area ID`),
  CONSTRAINT `rows_ibfk_1` FOREIGN KEY (`Area ID`) REFERENCES `areas` (`Area ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rows`
--

LOCK TABLES `rows` WRITE;
/*!40000 ALTER TABLE `rows` DISABLE KEYS */;
INSERT INTO `rows` VALUES ('R001','Abc','A001','hyd','1.2.3');
/*!40000 ALTER TABLE `rows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `site`
--

DROP TABLE IF EXISTS `site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `site` (
  `Site ID` varchar(255) NOT NULL,
  `Cust ID` varchar(255) DEFAULT NULL,
  `Site Name` varchar(255) NOT NULL,
  `Site Location` varchar(255) NOT NULL,
  `Site Owner Name` varchar(255) DEFAULT NULL,
  `Site GPS` varchar(255) NOT NULL,
  PRIMARY KEY (`Site ID`),
  KEY `Cust ID` (`Cust ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `site`
--

LOCK TABLES `site` WRITE;
/*!40000 ALTER TABLE `site` DISABLE KEYS */;
INSERT INTO `site` VALUES ('S001','','indisolar','Hyderabad, Telangana, India','Sunder raj','1.1');
/*!40000 ALTER TABLE `site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tables`
--

DROP TABLE IF EXISTS `tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tables` (
  `Table ID` varchar(255) NOT NULL,
  `Row ID` varchar(255) DEFAULT NULL,
  `Area ID` varchar(255) DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `GPS` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Table ID`),
  KEY `Row ID` (`Row ID`),
  KEY `Area ID` (`Area ID`),
  CONSTRAINT `tables_ibfk_1` FOREIGN KEY (`Row ID`) REFERENCES `rows` (`Row ID`),
  CONSTRAINT `tables_ibfk_2` FOREIGN KEY (`Area ID`) REFERENCES `areas` (`Area ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tables`
--

LOCK TABLES `tables` WRITE;
/*!40000 ALTER TABLE `tables` DISABLE KEYS */;
INSERT INTO `tables` VALUES ('T001','R001','A001','hyd','1.2.3');
/*!40000 ALTER TABLE `tables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_log`
--

DROP TABLE IF EXISTS `user_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_log` (
  `User ID` varchar(255) NOT NULL,
  `Date Logged in` datetime NOT NULL,
  `Date Logged out` datetime DEFAULT NULL,
  KEY `User ID` (`User ID`),
  CONSTRAINT `user_log_ibfk_1` FOREIGN KEY (`User ID`) REFERENCES `users` (`User ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_log`
--

LOCK TABLES `user_log` WRITE;
/*!40000 ALTER TABLE `user_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `User ID` varchar(255) NOT NULL,
  `Site ID` varchar(255) DEFAULT NULL,
  `User Name` varchar(255) NOT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Password` varchar(45) DEFAULT NULL,
  `User Designation` varchar(255) NOT NULL,
  `User Phone number` int NOT NULL,
  `User Type` varchar(255) NOT NULL,
  `Reports To` varchar(255) NOT NULL,
  `Date created` date DEFAULT NULL,
  `Date removed` date DEFAULT NULL,
  PRIMARY KEY (`User ID`),
  KEY `Site ID` (`Site ID`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`Site ID`) REFERENCES `site` (`Site ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('U001','S001','Naresh','nareshjanga966@gmail.com','123','Software Developer',1234567899,'Admin','sunder raj sir','2025-01-04',NULL),('U002','S001','naresh','nareshjanga@gmail.com','111','Software Developer',1234567899,'Normal User','123','2025-01-08',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-17 16:48:55
