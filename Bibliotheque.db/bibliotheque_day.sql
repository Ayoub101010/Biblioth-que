-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: bibliotheque
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `day`
--

DROP TABLE IF EXISTS `day`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `day` (
  `idday` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(45) DEFAULT NULL,
  `client` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `to_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  PRIMARY KEY (`idday`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `day`
--

LOCK TABLES `day` WRITE;
/*!40000 ALTER TABLE `day` DISABLE KEYS */;
INSERT INTO `day` VALUES (1,'Fenix','Ayoub','rent','2023-12-13','2023-12-14',NULL,NULL),(3,'Facebook','Ahmed','rent','2023-12-13','2023-12-19',NULL,NULL),(6,'Instagram','Akram','retrieve','2023-12-14',NULL,NULL,NULL),(7,'Instagram','Karima','retrieve','2023-12-14',NULL,NULL,NULL),(8,'Instagram','Wael','retrieve','2023-12-14',NULL,NULL,NULL),(9,'Twitter','sawsan','retrieve','2023-12-14',NULL,NULL,NULL),(10,'Facebook','Ahmed','retrieve','2023-12-14',NULL,NULL,NULL),(11,'Facebook','Kawtar','retrieve','2023-12-14','2023-12-15',NULL,NULL),(12,'Facebook','Anwar','retrieve','2023-12-14',NULL,NULL,'2023-12-14'),(13,'Facebook','Anwar','rent','2023-12-14','2023-12-15','2023-12-15',NULL),(14,'Facebook','Anwar','retrieve','2023-12-14',NULL,NULL,'2023-12-14');
/*!40000 ALTER TABLE `day` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-14 23:02:09
