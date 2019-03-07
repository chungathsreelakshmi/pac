/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.5.5-10.1.21-MariaDB : Database - pacs
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`pacs` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `pacs`;

/*Table structure for table `tbl_app_details` */

DROP TABLE IF EXISTS `tbl_app_details`;

CREATE TABLE `tbl_app_details` (
  `app_id` int(10) NOT NULL AUTO_INCREMENT,
  `bundle_id` int(10) DEFAULT NULL,
  `app_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`app_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_app_details` */

insert  into `tbl_app_details`(`app_id`,`bundle_id`,`app_name`) values (1,1,'app1'),(2,2,'app2'),(3,3,'app3'),(4,4,'app4');

/*Table structure for table `tbl_app_metadata` */

DROP TABLE IF EXISTS `tbl_app_metadata`;

CREATE TABLE `tbl_app_metadata` (
  `app_meta_id` int(10) NOT NULL AUTO_INCREMENT,
  `app_id` int(10) DEFAULT NULL,
  `permissions` varchar(50) DEFAULT NULL,
  `comments` text,
  `rating` varchar(50) DEFAULT NULL,
  `app_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`app_meta_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_app_metadata` */

insert  into `tbl_app_metadata`(`app_meta_id`,`app_id`,`permissions`,`comments`,`rating`,`app_status`) values (1,1,'per1','commentsssssssssss','3','active'),(2,2,'per2','comments','4','active');

/*Table structure for table `tbl_login` */

DROP TABLE IF EXISTS `tbl_login`;

CREATE TABLE `tbl_login` (
  `login_id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  `login_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_login` */

insert  into `tbl_login`(`login_id`,`username`,`password`,`user_type`,`login_status`) values (1,'admin','admin','admin','Active'),(2,'anu','anu','user','Active'),(3,'amal','amal','user','Blocked');

/*Table structure for table `tbl_user_apps` */

DROP TABLE IF EXISTS `tbl_user_apps`;

CREATE TABLE `tbl_user_apps` (
  `user_app_id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) DEFAULT NULL,
  `app_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`user_app_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_user_apps` */

insert  into `tbl_user_apps`(`user_app_id`,`user_id`,`app_id`) values (1,1,1),(2,1,3),(3,2,2),(4,2,4);

/*Table structure for table `tbl_users` */

DROP TABLE IF EXISTS `tbl_users`;

CREATE TABLE `tbl_users` (
  `user_id` int(10) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `u_imei` varchar(50) DEFAULT NULL,
  `u_fname` varchar(50) DEFAULT NULL,
  `u_lname` varchar(50) DEFAULT NULL,
  `u_phone` varchar(50) DEFAULT NULL,
  `u_email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_users` */

insert  into `tbl_users`(`user_id`,`login_id`,`u_imei`,`u_fname`,`u_lname`,`u_phone`,`u_email`) values (1,2,'364683646488','Anu','M','9876765454','anu@gmail.com'),(2,3,'897797987988','Amal','Dev','8886667433','amal@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
