// An array of links for navigation bar
const navBarLinks = [
  { name: "Home", url: "/" },
  { name: "Services", url: "/services" },
  { name: "About Us", url: "/about" },
  { name: "Blog", url: "/blog" },
  { name: "Contact", url: "/contact" },
];
// An array of links for footer
const footerLinks = [
  {
    section: "Services",
    links: [
      { name: "Business Consulting", url: "/services/business-consulting" },
      { name: "Digital Marketing", url: "/services/digital-marketing" },
      { name: "Social Media Marketing", url: "/services/social-media-marketing" },
      { name: "SEO Services", url: "/services/seo-services" },
    ],
  },
  {
    section: "Company",
    links: [
      { name: "About Us", url: "/about" },
      { name: "Services", url: "/services" },
      { name: "Blog", url: "/blog" },
      { name: "Contact", url: "/contact" },
    ],
  },
];
// An object of links for social icons
const socialLinks = {
  facebook: "https://www.facebook.com/tradeguildconsulting",
  linkedin: "https://www.linkedin.com/company/trade-guild-consulting/",
  instagram: "https://www.instagram.com/tradeguildconsulting/?igsh=MTExd25pcDgwM2QxNg%3D%3D#",
  tiktok: "https://www.tiktok.com/@guild.standard?_t=ZP-8ym5e9wcVWJ&_r=1",
  youtube: "https://youtube.com/@guildstandard?si=1XPfRisIrgH1Jfup",
};

export default {
  navBarLinks,
  footerLinks,
  socialLinks,
};
