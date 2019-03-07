/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.1.30-MariaDB : Database - pacs
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pacs` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `pacs`;

/*Table structure for table `tbl_login` */

DROP TABLE IF EXISTS `tbl_login`;

CREATE TABLE `tbl_login` (
  `login_id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  `login_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_login` */

insert  into `tbl_login`(`login_id`,`username`,`password`,`user_type`,`login_status`) values (1,'admin','admin','admin','Active'),(2,'anu','anu','user','Active'),(3,'amal','amal','user','Active'),(4,'jabi','jabi','user','Active'),(5,'jabi','jabi','user','Active'),(6,'jabi','jabi','user','Active'),(7,'jabi','jabi','user','Active'),(8,'jabi','jabi','user','Active'),(9,'jabi','jabi','user','Active');

/*Table structure for table `tbl_users` */

DROP TABLE IF EXISTS `tbl_users`;

CREATE TABLE `tbl_users` (
  `user_id` int(10) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `u_fname` varchar(50) DEFAULT NULL,
  `u_dob` date DEFAULT NULL,
  `u_lname` varchar(50) DEFAULT NULL,
  `u_phone` varchar(50) DEFAULT NULL,
  `u_email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_users` */

insert  into `tbl_users`(`user_id`,`login_id`,`u_fname`,`u_dob`,`u_lname`,`u_phone`,`u_email`) values (1,2,'Anu',NULL,'M','9876765454','anu@gmail.com'),(2,3,'Amal',NULL,'Dev','8886667433','amal@gmail.com'),(3,NULL,'Jabi','0000-00-00','kp','96325807411','jab@gm.com'),(4,7,'Jabi','0000-00-00','kp','96325807411','jab@gm.com'),(5,8,'Jabi','0000-00-00','kp','96325807411','jab@gm.com'),(6,9,'Jabi','0000-00-00','kp','96325807411','jab@gm.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
